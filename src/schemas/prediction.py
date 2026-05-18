"""
Pydantic schemas for API requests and responses
"""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class PredictionRequest(BaseModel):
    isic_id: Optional[str] = None

class PredictionResponse(BaseModel):
    isic_id: str
    probability: float = Field(..., ge=0.0, le=1.0)
    prediction: str
    model_version: str
    timestamp: datetime
    review_triggered: bool = False   

class HealthResponse(BaseModel):
    status: str
    model_version: str
    api_version: str
