🚀 FinScoreX Backend
This is the backend service for FinScoreX, a financial scoring system that evaluates business credit scores using machine learning. It is built with FastAPI and uses MongoDB for data storage.

📌 Features
✅ FastAPI-based API for high performance
✅ MongoDB integration for storing business financial data
✅ Machine Learning model to predict AI-based credit scores
✅ JWT authentication (optional future addition)
✅ CORS support for frontend integration

🛠 Tech Stack
FastAPI - API framework for high-speed applications
MongoDB - NoSQL database for storing business financial data
Motor (AsyncIO) - Asynchronous MongoDB client
NumPy, Scikit-Learn, Joblib - For AI-based credit score calculations
Uvicorn - ASGI server to run the FastAPI app
📂 Project Structure
graphql
Copy
Edit
FinScoreX_Backend/
│── models/
│   ├── model.py            # Pydantic data model for business records
│── routes/
│   ├── calculate_score.py   # API for calculating AI credit scores
│   ├── cibil_scores.py      # API for fetching CIBIL scores from MongoDB
│── ml/
│   ├── cibil_score_model.pkl  # Pre-trained ML model
│── database.py              # MongoDB connection setup
│── main.py                  # FastAPI entry point
│── requirements.txt          # Dependencies
🛠 Installation & Setup
1️⃣ Clone the repository

bash
Copy
Edit
git clone https://github.com/Pranav-Patel-123/FinScoreX_Backend.git
cd FinScoreX_Backend
2️⃣ Create a virtual environment & install dependencies

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
3️⃣ Set up environment variables
Create a .env file and add the MongoDB URI:

ini
Copy
Edit
MONGO_URI=mongodb+srv://your_mongodb_connection_string
4️⃣ Run the server

bash
Copy
Edit
uvicorn main:app --reload
📖 API Endpoints
Root
Method	Endpoint	Description
GET	/	Root API, checks if the server is running
Credit Score Calculation
Method	Endpoint	Description
POST	/calculate_score/	Calculate AI credit score & store data in MongoDB
Retrieve CIBIL Scores
Method	Endpoint	Description
GET	/cibil_scores/	Retrieve stored credit scores from MongoDB
📊 Machine Learning Model
The system uses a pre-trained ML model (cibil_score_model.pkl) to calculate AI-based credit scores based on financial inputs.

Key Features Considered in Score Calculation:
Loan Repayment History (Early Payment, Delayed, Defaulted)
Outstanding Debt & Monthly Revenue
Cash Flow Stability & Business Growth Rate
Supplier Payment Delay & Credit Default History
Macroeconomic Risks & Social Media Sentiment
The model normalizes input features and predicts a CIBIL Score.

🤝 Contributing
Fork the repository
Create a new branch (git checkout -b feature-branch)
Commit your changes (git commit -m "Added new feature")
Push to your branch (git push origin feature-branch)
Open a Pull Request
📜 License
This project is licensed under the MIT License.

Let me know if you need any modifications! 🚀🔥







