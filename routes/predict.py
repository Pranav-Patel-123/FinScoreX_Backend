from fastapi import APIRouter
import joblib
import numpy as np
from models.model import BusinessData

router = APIRouter()

# Load trained model
model = joblib.load("ml/cibil_score_model.pkl")

# Define categorical mappings
payment_history_mapping = {'Early Payment': 1.0, 'Delayed': 0.5, 'Defaulted': 0.0}

def calculate_score(data: BusinessData):
    """Computes AI credit score using the trained model."""
    
    # Convert categorical Loan Repayment History to numeric score
    payment_history_score = payment_history_mapping.get(data.Loan_Repayment_History, 0.5)

    # Compute Credit Utilization Ratio
    credit_utilization = data.Outstanding_Debt / max(data.Monthly_Revenue, 1)  # Avoid division by zero
    credit_utilization = min(credit_utilization, 1)  # Ensure within [0, 1]

    # Prepare features
    features = np.array([
        data.Outstanding_Debt, data.Monthly_Revenue, credit_utilization, payment_history_score,
        data.Years_in_Operation, data.Credit_Default_History, data.Supplier_Payment_Delay,
        data.Cash_Flow_Stability_Score, data.Business_Growth_Rate, data.Digital_Invoice_Payment_Rate,
        data.Macroeconomic_Risk_Score, data.Social_Media_Sentiment, data.Regulatory_Compliance_Score
    ]).reshape(1, -1)

    # Predict CIBIL Score
    score = model.predict(features)[0]
    return float(score)
