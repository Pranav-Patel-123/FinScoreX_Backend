from fastapi import APIRouter
from models.model import BusinessData
from models.database import collection
from ml.predict import calculate_score

router = APIRouter()

@router.post("/calculate_score/")
async def calculate_business_score(data: BusinessData):
    # Calculate AI Credit Score using ML model
    ai_score = calculate_score(data)

    # Convert to dictionary and store in MongoDB
    business_data = data.dict()
    business_data["AI_Credit_Score"] = ai_score  # Add calculated score

    # Insert data into MongoDB
    await collection.insert_one(business_data)

    return {
        "message": "Score calculated and stored successfully.",
        "Business_ID": data.Business_ID,
        "AI_Credit_Score": ai_score
    }
