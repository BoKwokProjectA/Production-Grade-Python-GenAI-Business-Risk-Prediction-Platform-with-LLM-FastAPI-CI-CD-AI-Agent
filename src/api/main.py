"""
Main FastAPI application.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.config import get_settings
from src.api.routes import prediction_router

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION,
    description="ISIC 2024 Skin Cancer Detection"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prediction_router)

@app.get("/api/v1/health")
async def health_check():
    return {
        "status": "healthy",
        "model_version": "2024-ensemble-models"
    }

@app.get("/")
async def root():
    return {"message": "ISIC 2024 Flagship API is running"}

