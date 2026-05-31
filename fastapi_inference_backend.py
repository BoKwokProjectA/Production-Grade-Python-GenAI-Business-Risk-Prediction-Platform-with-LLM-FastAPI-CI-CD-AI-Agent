#!/usr/bin/env python
# coding: utf-8

# In[22]:


from google.colab import drive
drive.mount('/content/drive', force_remount=True)


# In[23]:


import sys
import os

PROJECT_ROOT = "/content/drive/MyDrive/isic-flagship-project"
os.chdir(PROJECT_ROOT)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, "src"))

print(f"Working directory:", os.getcwd())


# In[24]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/core/config.py', '"""\nCore configuration\n"""\n\nfrom pydantic_settings import BaseSettings\nfrom functools import lru_cache\n\nclass Settings(BaseSettings):\n    APP_NAME: str = "ISIC 2024 Skin Cancer Detection"\n    API_VERSION: str = "v1"\n    MODEL_VERSION: str = "2024-ensemble-v1"\n    DEBUG: bool = True\n    DATABASE_URL: str = "sqlite+aiosqlite:///./isic.db"\n    NGROK_AUTHTOKEN: str = ""\n    SECRET_KEY: str = "super-secret-key-change-in-production"\n\n    class Config:\n        env_file = ".env"\n        env_file_encoding = "utf-8"\n\n\n@lru_cache()\ndef get_settings() -> Settings:\n    return Settings()\n\n\n')


# In[25]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/schemas/__init__.py', '')


# In[26]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/schemas/prediction.py', '"""\nPydantic schemas for API requests and responses\n"""\n\nfrom pydantic import BaseModel, Field\nfrom datetime import datetime\nfrom typing import Optional\n\nclass PredictionRequest(BaseModel):\n    isic_id: Optional[str] = None\n\nclass PredictionResponse(BaseModel):\n    isic_id: str\n    probability: float = Field(..., ge=0.0, le=1.0)\n    prediction: str\n    model_version: str\n    timestamp: datetime\n\nclass HealthResponse(BaseModel):\n    status: str\n    model_version: str\n    api_version: str\n\n')


# In[27]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/services/__init__.py', '')


# In[28]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/services/prediction_service.py', '"""\nBusiness logic for predictions\n"""\n\nimport torch\nfrom torchvision import transforms\nfrom PIL import Image\nimport io\n\nfrom src.inference.inference_core import ISICInferenceEngine\nfrom src.core.config import get_settings\n\nclass PredictionService:\n    def __init__(self):\n        self.settings = get_settings()\n        self.engine = ISICInferenceEngine()\n        self.transform = transforms.Compose([\n            transforms.Resize((224, 224)),\n            transforms.ToTensor(),\n            transforms.Normalize(mean=[0.485, 0.456, 0.406],\n                               std=[0.229, 0.224, 0.225]),\n        ])\n\n    async def predict(self, image_bytes):\n        """Process uploaded image and return prediction"""\n        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")\n        image_tensor = self.transform(image).unsqueeze(0)\n\n        prob = self.engine.predict_single_image(image_tensor)\n\n        prediction = "Malignant" if prob > 0.5 else "Benign"\n\n        return {\n             "probability": float(prob),\n             "prediction": prediction,\n             "model_version": self.settings.MODEL_VERSION\n        }\n\n\n\n')


# In[29]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/api/__init__.py', '')


# In[30]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/api/routes.py', '"""\nAPI Route definitions\n"""\n\nfrom fastapi import APIRouter, UploadFile, File, HTTPException\nfrom src.schemas.prediction import PredictionResponse, HealthResponse\nfrom src.services.prediction_service import PredictionService\nfrom src.core.config import get_settings\nfrom datetime import datetime\n\nprediction_service = PredictionService()\n\nhealth_router = APIRouter()\nprediction_router = APIRouter()\n\n@health_router.get("/health", response_model=HealthResponse)\nasync def health_check():\n    settings = get_settings()\n    return HealthResponse(\n        status="healthy",\n        model_version=settings.MODEL_VERSION,\n        api_version=settings.API_VERSION\n    )\n\n@prediction_router.post("/predict", response_model=PredictionResponse)\nasync def predict_image(file: UploadFile = File(...)):\n    if not file.content_type or not file.content_type.startswith("image/"):\n        raise HTTPException(status_code=400, detail="File must be an image")\n\n    image_bytes = await file.read()\n    result = await prediction_service.predict(image_bytes)\n\n    return PredictionResponse(\n        isic_id=file.filename or "uploaded_image",\n        probability=result["probability"],\n        prediction=result["prediction"],\n        model_version=result["model_version"],\n        timestamp=datetime.utcnow()\n    )\n\n')


# In[31]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/api/main.py', '"""\nMain FastAPI Application Entry Point\n"""\n\nfrom fastapi import FastAPI\nfrom fastapi.middleware.cors import CORSMiddleware\n\nfrom src.core.config import get_settings\nfrom src.api.routes import health_router, prediction_router\n\nsettings = get_settings()\n\napp = FastAPI(\n    title=settings.APP_NAME,\n    version=settings.API_VERSION,\n    description="Production-ready ISIC 2024 1st/2nd Place Skin Cancer Detection API"\n)\n\napp.add_middleware(\n    CORSMiddleware,\n    allow_origins=["*"],\n    allow_credentials=True,\n    allow_methods=["*"],\n    allow_headers=["*"],\n)\n\napp.include_router(health_router, prefix="/api/v1", tags=["health"])\napp.include_router(prediction_router, prefix="/api/v1", tags=["prediction"])\n\n@app.get("/")\nasync def root():\n    return {\n        "message": "ISIC 2024 Flagship API is running 🚀",\n        "docs_url": "/docs"\n    }\n\n')

