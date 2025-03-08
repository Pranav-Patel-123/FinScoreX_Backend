from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI on Vercel!"}

# Vercel expects an ASGI handler called `handler`
from mangum import Mangum
handler = Mangum(app)  # Wrap FastAPI with Mangum for AWS Lambda compatibility
