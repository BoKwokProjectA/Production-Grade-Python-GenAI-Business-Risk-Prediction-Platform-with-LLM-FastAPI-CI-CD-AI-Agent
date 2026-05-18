"""
API routes for skin lesion prediction.
"""
from fastapi import APIRouter, UploadFile, File, HTTPException
from datetime import datetime
from src.services.prediction_service import PredictionService
from src.schemas.prediction import PredictionResponse

prediction_service = PredictionService()
prediction_router = APIRouter(prefix="/api/v1", tags=["prediction"])

@prediction_router.post("/predict", response_model=PredictionResponse,
    summary="Predict skin lesion risk",
    description="""
    Upload a dermoscopy image to get malignant risk prediction.
    
    **Human-in-the-Loop Safety Feature:**
    - If probability is between 0.45 and 0.55, the system automatically triggers 
      a human review via Power Automate.
    - The field `review_triggered` will be `true` in such cases.
    """)
async def predict_image(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    result = await prediction_service.predict(file)
    
    return PredictionResponse(
        isic_id=file.filename or "uploaded_image",
        probability=result["probability"],
        prediction=result["prediction"],
        model_version=result.get("model_version", "2024-ensemble-2models"),
        timestamp=datetime.utcnow(),
        review_triggered=(0.45 <= result["probability"] <= 0.55)
    )
