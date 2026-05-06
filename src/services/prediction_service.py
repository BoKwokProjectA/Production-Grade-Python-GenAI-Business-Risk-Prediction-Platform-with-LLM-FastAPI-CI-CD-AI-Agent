"""
Business logic for predictions
"""

import torch
from torchvision import transforms
from PIL import Image
import io

from src.inference.inference_core import ISICInferenceEngine
from src.core.config import get_settings

class PredictionService:
    def __init__(self):
        self.settings = get_settings()
        self.engine = ISICInferenceEngine()
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                               std=[0.229, 0.224, 0.225]),
        ])

    async def predict(self, image_bytes):
        """Process uploaded image and return prediction"""
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image_tensor = self.transform(image).unsqueeze(0)
        
        prob = self.engine.predict_single_image(image_tensor)

        prediction = "Malignant" if prob > 0.5 else "Benign"

        return {
             "probability": float(prob),
             "prediction": prediction,
             "model_version": self.settings.MODEL_VERSION
        }



