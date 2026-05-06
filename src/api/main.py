"""
Main FastAPI Application Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.config import get_settings
from src.api.routes import health_router, prediction_router

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION,
    description="Production-ready ISIC 2024 1st/2nd Place Skin Cancer Detection API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api/v1", tags=["health"])
app.include_router(prediction_router, prefix="/api/v1", tags=["prediction"])

@app.get("/")
async def root():
    return {
        "message": "ISIC 2024 Flagship API is running 🚀",
        "docs_url": "/docs"
    }

