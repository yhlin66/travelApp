from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.settings import Settings
from routers import (
    users,
    # travel_plans,
    ai_agents
)
from services import ai_agents as ai_agents_service
from models import user, travel_plan
import uvicorn
from typing import Dict
app = FastAPI(title="Travel Share Platform API")

# CORS 設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在正式環境中要設定具體的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 註冊路由
app.include_router(users.router, prefix="/api/users", tags=["users"])
# app.include_router(travel_plans.router, prefix="/api/travel-plans", tags=["travel_plans"])
app.include_router(ai_agents.router, prefix="/api/ai", tags=["ai_agents"]) 


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Travel Planner API"}


@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
