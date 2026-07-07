from fastapi import FastAPI
from app.api import health

app = FastAPI(title="AIRouter-Pro", version="0.1.0")

app.include_router(health.router, tags=["health"])


@app.get("/")
def root():
    return {"message": "AIRouter-Pro is running"}