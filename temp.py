import pandas as pd
import pymongo

# MongoDB connection
MONGO_URI = "mongodb+srv://test:3dGQuUYsGJiehTSl@cluster0.yttrefz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Replace with your MongoDB URI
DATABASE_NAME = "business_db"
COLLECTION_NAME = "business_data"

# Connect to MongoDB
client = pymongo.MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Read CSV file
csv_file_path = "updated_cibil_score_dataset.csv"  # Update if necessary
df = pd.read_csv(csv_file_path)

# Convert DataFrame to JSON format
data = df.to_dict(orient="records")

# Insert data into MongoDB
result = collection.insert_many(data)

print(f"Inserted {len(result.inserted_ids)} records into MongoDB successfully!")
