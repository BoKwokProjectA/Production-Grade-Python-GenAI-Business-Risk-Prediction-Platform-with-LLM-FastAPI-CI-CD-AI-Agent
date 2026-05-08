"""
Prediction service that uses the real ensemble engine.
"""

from fastapi import UploadFile
from PIL import Image
import io
from src.inference.ensemble_engine import ISICEnsembleEngine

class PredictionService:
    def __init__(self):
        self.engine = ISICEnsembleEngine()

    async def predict(self, file: UploadFile):
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        
        self.engine.load_models()
        result = self.engine.predict(image)   
        
        return {
            "probability": result["probability"],
            "prediction": result["prediction"],
            "model_version": "2024-ensemble-2models"
        }
