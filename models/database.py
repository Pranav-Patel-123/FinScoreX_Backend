from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment variable
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = "business_db"

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGO_URI)
database = client[DATABASE_NAME]
collection = database["business_data"]
