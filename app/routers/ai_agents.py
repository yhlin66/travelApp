from fastapi import APIRouter, HTTPException
from services.ai_agents import WeatherExpert, TravelExpert, FlightExpert, PlanningExpert
from typing import Dict

router = APIRouter()

@router.post("/weather/{location}")
async def get_weather_info(location: str):
    try:
        weather_expert = WeatherExpert()
        return await weather_expert.get_weather_info(location)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/travel-info/{location}")
async def get_travel_info(location: str):
    # 實作旅遊資訊端點
    pass

@router.post("/flight-info")
async def get_flight_info(departure: str, destination: str, date: str):
    # 實作機票資訊端點
    pass

@router.post("/create-plan")
async def create_travel_plan(params: Dict):
    # 實作旅遊計畫生成端點
    pass 