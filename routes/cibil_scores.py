from fastapi import APIRouter, HTTPException
from models.database import collection


router = APIRouter()


@router.get("/")
async def get_cibil_scores():
    try:
        # Fetch all data from MongoDB
        raw_data = await collection.find({}).to_list(None)

        print("📦 Fetched Data from MongoDB:", raw_data)  # Debugging log

        if not raw_data:
            raise HTTPException(status_code=404, detail="No data found")

        # Extract all unique months and sort them
        all_months = sorted(set(doc.get("Month", "") for doc in raw_data if doc.get("Month")))

        # Process data and calculate previous scores
        formatted_data = []

        # Group data by Business_ID
        business_data = {}
        for doc in raw_data:
            business_id = doc.get("Business_ID", "Unknown")
            if business_id not in business_data:
                business_data[business_id] = []
            business_data[business_id].append(doc)

        # Sort records for each business by month
        for business_id, records in business_data.items():
            records.sort(key=lambda x: all_months.index(x["Month"]))  # Sort by month order
            
            previous_score = None
            for doc in records:
                month = doc["Month"]
                date = doc.get("Date", "")  # Fetch the date
                score = doc["AI_Credit_Score"]

                formatted_data.append({
                    "_id": str(doc["_id"]),
                    "businessId": business_id,
                    "businessType": doc.get("Business_Type", ""),
                    "industrySector": doc.get("Industry_Sector", ""),
                    "month": month,
                    "date": date,  # Include date field
                    "score": score,
                    "previousScore": previous_score if previous_score is not None else score  # Keep same score if no previous month data
                })

                # Update previous score for the next record
                previous_score = score

        print("✅ Final formatted response:", formatted_data)  # Debug log

        return {"months": all_months, "data": formatted_data}

    except Exception as e:
        print("🔥 ERROR:", str(e))  # Log error
        raise HTTPException(status_code=500, detail="Server error: " + str(e))
