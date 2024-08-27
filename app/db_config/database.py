import motor.motor_asyncio
from app.config import settings

try:
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongoDB_url)
    collection = client.sample_airbnb
except Exception as e:
    print(e)
