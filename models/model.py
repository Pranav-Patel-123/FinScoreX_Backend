from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

# Helper class to convert MongoDB ObjectId to string
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v)

class BusinessData(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)  # MongoDB's default _id field
    Business_ID: str  # Unique identifier for the business
    Business_Type: str
    Industry_Sector: str
    Years_in_Operation: int
    Monthly_Revenue: float
    Monthly_Expenses: float
    Loan_Repayment_History: str
    Outstanding_Debt: float
    Cash_Flow_Stability_Score: float
    GST_Filings: int
    Supplier_Payment_Delay: int
    Ecommerce_Sales_Volume: float
    Digital_Invoice_Payment_Rate: float
    Credit_Default_History: int
    Business_Growth_Rate: float
    Macroeconomic_Risk_Score: float
    Social_Media_Sentiment: float
    Regulatory_Compliance_Score: float
    Month: str

    # AI_Credit_Score is optional and will be calculated
    AI_Credit_Score: Optional[float] = None

    class Config:
        json_encoders = {ObjectId: str}  # Convert ObjectId to string in JSON responses
