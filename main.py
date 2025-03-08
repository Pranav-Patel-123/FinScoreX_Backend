from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.cibil_scores import router as cibil_scores_router
from routes.calculate_score import router as calculate_score_router
 
app = FastAPI(title="Business Credit Score API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, or specify ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(cibil_scores_router)
app.include_router(calculate_score_router)

@app.get("/")
async def root():
    return {"message": "CIBIL Score API is running!"}