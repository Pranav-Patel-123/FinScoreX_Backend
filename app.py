import uvicorn
from api.main import app  # Importing FastAPI app from api/main.py

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)