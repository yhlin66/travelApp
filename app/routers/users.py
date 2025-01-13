from fastapi import APIRouter, HTTPException, Depends
from models.user import UserCreate, UserInDB
from services.auth import get_current_user, create_access_token
from services.user import UserService
from typing import Dict

router = APIRouter()


@router.post("/register")
async def register_user(user: UserCreate) -> Dict:
    user_service = UserService()
    try:
        new_user = await user_service.create_user(user)
        return {"message": "註冊成功", "user_id": new_user.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
async def login(email: str, password: str) -> Dict:
    user_service = UserService()
    user = await user_service.authenticate_user(email, password)
    if not user:
        raise HTTPException(status_code=401, detail="帳號或密碼錯誤")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me")
async def get_current_user_info(current_user: UserInDB = Depends(get_current_user)):
    return current_user
