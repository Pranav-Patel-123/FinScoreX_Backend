from fastapi import FastAPI
from routes import calculate_score, cibil_scores, predict, scoring

app = FastAPI()

# Include routes
app.include_router(calculate_score.router, prefix="/calculate", tags=["Calculate Score"])
app.include_router(cibil_scores.router, prefix="/cibil", tags=["CIBIL Scores"])
app.include_router(predict.router, prefix="/predict", tags=["Prediction"])
app.include_router(scoring.router, prefix="/scoring", tags=["Scoring"])

__all__ = ["app"]
