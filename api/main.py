from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.cibil_scores import router as cibil_scores_router
from routes.calculate_score import router as calculate_score_router

# Initialize FastAPI app
app = FastAPI(title="Business Credit Score API", version="1.0", description="API for Business Credit Score Calculation")

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins; change to specific domains for security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Register routers
app.include_router(cibil_scores_router, prefix="/cibil", tags=["CIBIL Scores"])
app.include_router(calculate_score_router, prefix="/calculate", tags=["Credit Score Calculation"])

@app.get("/", tags=["Health Check"])
async def root():
    return {"message": "CIBIL Score API is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="0.0.0.0", port=7860, reload=True)
