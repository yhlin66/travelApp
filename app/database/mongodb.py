from motor.motor_asyncio import AsyncIOMotorClient
from config.settings import Settings

settings = Settings()
client = AsyncIOMotorClient(settings.MONGODB_URL)
database = client[settings.DATABASE_NAME]


def get_database():
    return database
