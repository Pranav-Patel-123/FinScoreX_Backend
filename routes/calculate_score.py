import joblib
import numpy as np
from fastapi import APIRouter, HTTPException
from models.model import BusinessData
from models.database import collection

router = APIRouter()

# Load trained model
try:
    model = joblib.load("ml/cibil_score_model.pkl")
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

# Define categorical mappings
payment_history_mapping = {'Early Payment': 1.0, 'Delayed': 0.5, 'Defaulted': 0.0}

def calculate_score(data: BusinessData) -> float:
    """Computes AI credit score using the trained model."""

    try:
        # Convert categorical Loan Repayment History to numeric score
        payment_history_score = payment_history_mapping.get(data.Loan_Repayment_History, 0.5)

        # Compute Credit Utilization Ratio
        credit_utilization = data.Outstanding_Debt / max(data.Monthly_Revenue, 1)  # Avoid division by zero
        credit_utilization = min(credit_utilization, 1)  # Ensure within [0, 1]

        # Prepare feature array for the model
        features = np.array([
            data.Outstanding_Debt, data.Monthly_Revenue, credit_utilization, payment_history_score,
            data.Years_in_Operation, data.Credit_Default_History, data.Supplier_Payment_Delay,
            data.Cash_Flow_Stability_Score, data.Business_Growth_Rate, data.Digital_Invoice_Payment_Rate,
            data.Macroeconomic_Risk_Score, data.Social_Media_Sentiment, data.Regulatory_Compliance_Score
        ]).reshape(1, -1)

        # Predict CIBIL Score
        score = model.predict(features)[0]
        return float(score)

    except Exception as e:
        raise ValueError(f"Error in score calculation: {e}")

@router.post("/")
async def calculate_business_score(data: BusinessData):
    try:
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

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {e}")
