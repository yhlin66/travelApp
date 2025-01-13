from models.user import UserCreate, UserInDB
from datetime import datetime
import bcrypt
from typing import Optional
from database.mongodb import get_database


class UserService:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.users

    async def create_user(self, user: UserCreate) -> UserInDB:
        # 檢查是否已存在相同 email
        if await self.get_user_by_email(user.email):
            raise ValueError("此 email 已被註冊")

        # 密碼加密
        hashed_password = bcrypt.hashpw(
            user.password.encode(), bcrypt.gensalt())

        user_dict = {
            "email": user.email,
            "name": user.name,
            "hashed_password": hashed_password,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }

        result = await self.collection.insert_one(user_dict)
        user_dict["id"] = str(result.inserted_id)
        return UserInDB(**user_dict)

    async def get_user_by_email(self, email: str) -> Optional[UserInDB]:
        user = await self.collection.find_one({"email": email})
        if user:
            user["id"] = str(user["_id"])
            return UserInDB(**user)
        return None

    async def authenticate_user(self, email: str, password: str) -> Optional[UserInDB]:
        user = await self.get_user_by_email(email)
        if not user:
            return None
        if not bcrypt.checkpw(password.encode(), user.hashed_password):
            return None
        return user
