from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class TravelPlan(BaseModel):
    id: str
    user_id: str
    destination: str
    start_date: datetime
    end_date: datetime
    budget: float
    preferences: dict  # 存儲旅遊偏好
    weather_info: Optional[dict]
    travel_info: Optional[dict]
    flight_info: Optional[dict]
    itinerary: Optional[List[dict]] 