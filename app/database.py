from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")  # From your MongoDB Atlas cluster
client = AsyncIOMotorClient(MONGO_URI)
db = client["ecommerce"]
