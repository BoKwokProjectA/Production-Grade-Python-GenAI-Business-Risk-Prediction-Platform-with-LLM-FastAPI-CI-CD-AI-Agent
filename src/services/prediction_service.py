"""
Prediction service with Power Automate human review trigger.
"""

import io
from datetime import datetime, timezone

import httpx
from fastapi import UploadFile
from PIL import Image

from src.inference.ensemble_engine import ISICEnsembleEngine
from src.core.config import get_settings


class PredictionService:
    def __init__(self):
        self.engine = ISICEnsembleEngine()
        self.settings = get_settings()
        self.engine.load_models()

    async def predict(self, file: UploadFile):
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        result = self.engine.predict(image)

        probability = float(result["probability"])

        if 0.45 <= probability <= 0.55:
            await self._trigger_power_automate_review(result)

        result["probability"] = probability
        return result

    async def _trigger_power_automate_review(self, result):
        url = self.settings.POWER_AUTOMATE_URL

        if not url:
            return

        payload = {
            "isic_id": str(result.get("isic_id", "uploaded_image")),
            "probability": float(result["probability"]),
            "prediction": str(result["prediction"]),
            "image_filename": str(result.get("image_filename", "unknown.jpg")),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        try:
            async with httpx.AsyncClient(timeout=15.0) as client:
                await client.post(url, json=payload)
        except Exception:
            pass
