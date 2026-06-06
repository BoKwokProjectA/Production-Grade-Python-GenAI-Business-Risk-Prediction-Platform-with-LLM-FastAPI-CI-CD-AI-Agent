"""
Prediction service with lazy model loading and optional Power Automate review trigger.
"""

import io
from datetime import UTC, datetime

import httpx
from fastapi import UploadFile
from PIL import Image

from src.core.config import get_settings
from src.inference.ensemble_engine import ISICEnsembleEngine


class PredictionService:
    def __init__(self):
        self.settings = get_settings()
        self.engine = None

    def _get_engine(self) -> ISICEnsembleEngine:
        if self.engine is None:
            self.engine = ISICEnsembleEngine()
        return self.engine

    async def predict(self, file: UploadFile):
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        result = self._get_engine().predict(image)
        probability = float(result["probability"])

        if 0.45 <= probability <= 0.55:
            await self._trigger_power_automate_review(result)

        result["probability"] = probability
        result.setdefault("model_version", self.settings.MODEL_VERSION)
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
            "timestamp": datetime.now(UTC).isoformat(),
        }

        try:
            async with httpx.AsyncClient(timeout=15.0) as client:
                await client.post(url, json=payload)
        except Exception:
            pass
