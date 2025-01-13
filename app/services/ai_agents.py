from typing import Dict
import google.generativeai as genai
from config.settings import Settings

class BaseAgent:
    def __init__(self):
        genai.configure(api_key=Settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')

class WeatherExpert(BaseAgent):
    async def get_weather_info(self, location: str) -> Dict:
        prompt = f"""作為天氣專家，請提供{location}的天氣資訊：
        1. 年平均氣溫
        2. 季節性天氣特點
        3. 最佳旅遊季節
        請只提供公開的統計資訊，不要進行天氣預測。
        """
        response = await self.model.generate_content(prompt)
        return response.text

class TravelExpert(BaseAgent):
    async def get_travel_info(self, location: str) -> Dict:
        # 實作旅遊資訊查詢邏輯
        pass

class FlightExpert(BaseAgent):
    async def get_flight_info(self, departure: str, destination: str, date: str) -> Dict:
        # 實作機票資訊查詢邏輯
        pass

class PlanningExpert(BaseAgent):
    async def create_travel_plan(self, params: Dict) -> Dict:
        # 實作旅遊計畫生成邏輯
        pass 