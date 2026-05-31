#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from google.colab import drive
drive.mount('/content/drive', force_remount=True)


# In[ ]:


import os
from pathlib import Path

PROJECT_ROOT = "/content/drive/MyDrive/isic-flagship-project"
os.chdir(PROJECT_ROOT)


# In[ ]:


get_ipython().run_cell_magic('writefile', 'src/inference/ensemble_engine.py', '"""\nEnsemble inference for ISIC 2024 skin lesion prediction.\n"""\n\nimport torch\nimport timm\nimport numpy as np\nfrom PIL import Image\nimport torchvision.transforms as T\nfrom pathlib import Path\n\nPROJECT_ROOT = Path("/content/drive/MyDrive/isic-flagship-project")\n\nclass ISICEnsembleEngine:\n    def __init__(self):\n        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")\n        self.models = []\n        self.transforms = []\n        self.models_loaded = False\n\n    def load_models(self):\n        if self.models_loaded:\n            return\n\n        model1 = timm.create_model(\'convnext_small\', pretrained=True, num_classes=2)\n        model1 = model1.to(self.device).eval()\n        self.models.append(model1)\n        self.transforms.append(T.Compose([\n            T.Resize(384), T.CenterCrop(384), T.ToTensor(),\n            T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),\n        ]))\n\n        model2 = timm.create_model(\'eva02_small_patch14_336\', pretrained=True, num_classes=2)\n        model2 = model2.to(self.device).eval()\n        self.models.append(model2)\n        self.transforms.append(T.Compose([\n            T.Resize(336), T.CenterCrop(336), T.ToTensor(),\n            T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),\n        ]))\n\n        self.models_loaded = True\n\n    def predict(self, image: Image.Image = None):\n        if not self.models_loaded:\n            self.load_models()\n\n        if image is None:\n            image = Image.fromarray(np.random.randint(0, 255, (384, 384, 3), dtype=np.uint8))\n\n        probs = []\n        with torch.no_grad():\n            for i, model in enumerate(self.models):\n                input_tensor = self.transforms[i](image).unsqueeze(0).to(self.device)\n                logits = model(input_tensor)\n                prob = torch.softmax(logits, dim=1)[:, 1].item()\n                probs.append(prob)\n\n        final_prob = np.mean(probs)\n\n        return {\n            "probability": final_prob,\n            "prediction": "benign" if final_prob < 0.5 else "malignant"\n        }\n')


# In[ ]:


get_ipython().run_cell_magic('writefile', 'src/services/prediction_service.py', '"""\nPrediction service that uses the real ensemble engine.\n"""\n\nfrom fastapi import UploadFile\nfrom PIL import Image\nimport io\nfrom src.inference.ensemble_engine import ISICEnsembleEngine\n\nclass PredictionService:\n    def __init__(self):\n        self.engine = ISICEnsembleEngine()\n\n    async def predict(self, file: UploadFile):\n        image_bytes = await file.read()\n        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")\n\n        self.engine.load_models()\n        result = self.engine.predict(image)\n\n        return {\n            "probability": result["probability"],\n            "prediction": result["prediction"],\n            "model_version": "2024-ensemble-2models"\n        }\n')


# In[ ]:


get_ipython().run_cell_magic('writefile', 'src/api/routes.py', '"""\nAPI routes for skin lesion prediction.\n"""\n\nfrom fastapi import APIRouter, UploadFile, File, HTTPException\nfrom datetime import datetime\nfrom src.services.prediction_service import PredictionService\nfrom src.schemas.prediction import PredictionResponse\n\nprediction_service = PredictionService()\nprediction_router = APIRouter(prefix="/api/v1", tags=["prediction"])\n\n@prediction_router.post("/predict", response_model=PredictionResponse)\nasync def predict_image(file: UploadFile = File(...)):\n    if not file.content_type or not file.content_type.startswith("image/"):\n        raise HTTPException(status_code=400, detail="File must be an image")\n\n    result = await prediction_service.predict(file)\n\n    return PredictionResponse(\n        isic_id=file.filename or "uploaded_image",\n        probability=result["probability"],\n        prediction=result["prediction"],\n        model_version=result["model_version"],\n        timestamp=datetime.utcnow()\n    )\n')


# In[ ]:


get_ipython().run_cell_magic('writefile', 'src/api/main.py', '"""\nMain FastAPI application.\n"""\n\nfrom fastapi import FastAPI\nfrom fastapi.middleware.cors import CORSMiddleware\nfrom src.core.config import get_settings\nfrom src.api.routes import prediction_router\n\nsettings = get_settings()\n\napp = FastAPI(\n    title=settings.APP_NAME,\n    version=settings.API_VERSION,\n    description="ISIC 2024 Skin Cancer Detection"\n)\n\napp.add_middleware(\n    CORSMiddleware,\n    allow_origins=["*"],\n    allow_methods=["*"],\n    allow_headers=["*"],\n)\n\napp.include_router(prediction_router)\n\n@app.get("/api/v1/health")\nasync def health_check():\n    return {\n        "status": "healthy",\n        "model_version": "2024-ensemble-models"\n    }\n\n@app.get("/")\nasync def root():\n    return {"message": "ISIC 2024 Flagship API is running"}\n\n')


# In[ ]:




