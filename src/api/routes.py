"""
API Route definitions
"""

from fastapi import APIRouter, UploadFile, File, HTTPException
from src.schemas.prediction import PredictionResponse, HealthResponse
from src.services.prediction_service import PredictionService
from src.core.config import get_settings  
from datetime import datetime

prediction_service = PredictionService()

health_router = APIRouter()
prediction_router = APIRouter()

@health_router.get("/health", response_model=HealthResponse)
async def health_check():
    settings = get_settings()
    return HealthResponse(
        status="healthy",
        model_version=settings.MODEL_VERSION,
        api_version=settings.API_VERSION
    )

@prediction_router.post("/predict", response_model=PredictionResponse)
async def predict_image(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    image_bytes = await file.read()
    result = await prediction_service.predict(image_bytes)

    return PredictionResponse(
        isic_id=file.filename or "uploaded_image",
        probability=result["probability"],
        prediction=result["prediction"],
        model_version=result["model_version"],
        timestamp=datetime.utcnow()
    )

