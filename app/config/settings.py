from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # 資料庫設定
    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "travel_planner"

    # JWT 設定
    SECRET_KEY: str = "your-secret-key"  # 請在生產環境中更改
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # AI API 金鑰
    GEMINI_API_KEY: Optional[str] = None

    class Config:
        env_file = ".env"
