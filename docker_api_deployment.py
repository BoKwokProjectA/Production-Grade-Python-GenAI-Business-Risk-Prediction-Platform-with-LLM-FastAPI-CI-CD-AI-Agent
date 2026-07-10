#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from google.colab import drive
drive.mount('/content/drive', force_remount=True)


# In[ ]:


import os
from pathlib import Path

PROJECT_ROOT = Path("/content/drive/MyDrive/isic-flagship-project")
os.chdir(PROJECT_ROOT)

print("Working in:", PROJECT_ROOT)


# In[ ]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/api/main.py', '"""\nCloud Run entry point for the Copilot Studio support API.\n"""\n\nfrom fastapi import FastAPI\nfrom fastapi.middleware.cors import CORSMiddleware\n\n\n\napp = FastAPI(\n    title="ISIC Skin Lesion Platform Support API",\n    version="1.0.0",\n    description="Lightweight API used by the Copilot Studio support agent.",\n)\n\napp.add_middleware(\n    CORSMiddleware,\n    allow_origins=["*"],\n    allow_credentials=True,\n    allow_methods=["*"],\n    allow_headers=["*"],\n)\n\n\n@app.get("/")\nasync def root():\n    return {\n        "status": "ok",\n        "service": "ISIC Copilot Support API",\n    }\n\n\n@app.get("/api/v1/health")\nasync def health():\n    return {\n        "status": "ok",\n        "service": "copilot-support-api",\n    }\n\n\napp.include_router(\n    copilot_router,\n    prefix="/api/v1",\n    tags=["copilot-studio"],\n)\n')


# In[ ]:


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes import health_router, prediction_router

app = FastAPI(
    title="ISIC 2024 Skin Cancer Detection API",
    version="1.0.0",
    description="ISIC Skin Lesion Platform API with image prediction endpoints",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "status": "ok",
        "service": "ISIC Skin Lesion Platform API",
        "docs_url": "/docs",
    }

app.include_router(health_router, prefix="/api/v1", tags=["health"])
app.include_router(prediction_router, prefix="/api/v1", tags=["prediction"])


# In[ ]:


import os
import sys
from pathlib import Path

PROJECT_ROOT = Path("/content/drive/MyDrive/isic-flagship-project")
os.chdir(PROJECT_ROOT)

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))



routes = sorted(route.path for route in app.routes)

print("App import OK")
print("Routes:")
for route in routes:
    print("-", route)

assert "/api/v1/health" in routes
assert "/api/v1/predict" in routes

assert "/api/v1/agent/health" not in routes
assert "/api/v1/agent/support" not in routes


# In[ ]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/Dockerfile', 'FROM python:3.11-slim\n\nWORKDIR /app\n\nENV PYTHONDONTWRITEBYTECODE=1\nENV PYTHONUNBUFFERED=1\n\nRUN apt-get update && apt-get install -y \\\n    git \\\n    curl \\\n    libgl1 \\\n    libglib2.0-0 \\\n    && rm -rf /var/lib/apt/lists/*\n\nCOPY requirements.txt .\n\nRUN pip install --upgrade pip\n\nRUN pip install --no-cache-dir \\\n    torch==2.3.1 \\\n    torchvision==0.18.1 \\\n    --index-url https://download.pytorch.org/whl/cpu\n\nRUN pip install --no-cache-dir -r requirements.txt\n\nCOPY src/ ./src/\nCOPY .env.example .env\n\nEXPOSE 8080\n\nCMD exec uvicorn src.api.main:app --host 0.0.0.0 --port ${PORT:-8080}\n')


# In[ ]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/requirements.txt', 'fastapi==0.115.2\nuvicorn[standard]==0.32.0\npydantic==2.9.2\npydantic-settings==2.6.1\nsqlalchemy==2.0.35\nalembic==1.13.2\naiosqlite==0.20.0\npython-dotenv==1.0.1\npandas==2.2.2\nnumpy==1.26.4\npillow==10.4.0\ntimm==1.0.11\nlightgbm==4.5.0\ncatboost==1.2.7\nxgboost==2.1.1\nscikit-learn==1.5.2\nlangchain==0.3.4\nlangchain-community==0.3.3\nlangchain-text-splitters==0.3.0\nfaiss-cpu==1.8.0.post1\nsentence-transformers==3.1.1\npython-multipart==0.0.9\nhttpx==0.27.2\nstructlog==24.4.0\n')


# In[ ]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/.dockerignore', '__pycache__/\n*.pyc\n*.pyo\n*.pyd\n.Python\nenv/\nvenv/\n.venv/\n.git/\n.gitignore\n.ipynb_checkpoints/\n*.ipynb\nlogs/\n')


# In[ ]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/api/main.py', '"""\nMain FastAPI application.\n"""\n\nfrom fastapi import FastAPI\nfrom fastapi.middleware.cors import CORSMiddleware\n\nfrom src.core.config import get_settings\nfrom src.api.routes import health_router, prediction_router\n\n\nsettings = get_settings()\n\napp = FastAPI(\n    title="ISIC Skin Lesion Platform API",\n    version=settings.API_VERSION,\n    description="ISIC Skin Lesion Platform API with image prediction endpoints",\n)\n\napp.add_middleware(\n    CORSMiddleware,\n    allow_origins=["*"],\n    allow_credentials=True,\n    allow_methods=["*"],\n    allow_headers=["*"],\n)\n\n\n@app.get("/")\nasync def root():\n    return {\n        "status": "ok",\n        "service": "ISIC Skin Lesion Platform API",\n        "docs_url": "/docs",\n        "openapi_url": "/openapi.json",\n    }\n\n\napp.include_router(\n    health_router,\n    prefix="/api/v1",\n    tags=["health"],\n)\n\napp.include_router(\n    prediction_router,\n    prefix="/api/v1",\n    tags=["prediction"],\n)\n\napp.include_router(\n    copilot_router,\n    prefix="/api/v1",\n    tags=["copilot-studio"],\n)\n')


# In[ ]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/api/routes.py', '"""\nAPI routes for skin lesion prediction.\n"""\n\nfrom datetime import datetime\n\nfrom fastapi import APIRouter, UploadFile, File, HTTPException\n\nfrom src.core.config import get_settings\nfrom src.schemas.prediction import PredictionResponse, HealthResponse\nfrom src.services.prediction_service import PredictionService\n\n\nsettings = get_settings()\n\nhealth_router = APIRouter()\nprediction_router = APIRouter()\n\nprediction_service = PredictionService()\n\n\n@health_router.get("/health", response_model=HealthResponse)\nasync def health_check():\n    return HealthResponse(\n        status="healthy",\n        model_version=settings.MODEL_VERSION,\n        api_version=settings.API_VERSION,\n    )\n\n\n@prediction_router.post(\n    "/predict",\n    response_model=PredictionResponse,\n    summary="Expand the block to predict skin lesion risk",\n    description="""\nUpload a skin lesion image and receive a malignant-risk prediction.\n\nIf the probability is in the review boundary range, the backend may trigger\na human-review workflow depending on the active PredictionService implementation.\n""",\n)\nasync def predict_image(file: UploadFile = File(...)):\n    if not file.content_type or not file.content_type.startswith("image/"):\n        raise HTTPException(status_code=400, detail="File must be an image")\n\n    result = await prediction_service.predict(file)\n\n    probability = float(result["probability"])\n\n    return PredictionResponse(\n        isic_id=file.filename or "uploaded_image",\n        probability=probability,\n        prediction=result["prediction"],\n        model_version=result.get("model_version", settings.MODEL_VERSION),\n        timestamp=datetime.utcnow(),\n        review_triggered=result.get(\n            "review_triggered",\n            0.45 <= probability <= 0.55,\n        ),\n    )\n')


# In[ ]:


from google.colab import auth
auth.authenticate_user()


# In[ ]:


PROJECT_ID = "isic-flagship-project"
REGION = "europe-west2"
SERVICE_NAME = "isic-api"

get_ipython().system('gcloud config set project {PROJECT_ID}')


# In[ ]:


PROJECT_NUMBER = get_ipython().getoutput('gcloud projects describe {PROJECT_ID} --format="value(projectNumber)"')
PROJECT_NUMBER = PROJECT_NUMBER[0]

SERVICE_ACCOUNT = f"{PROJECT_NUMBER}-compute@developer.gserviceaccount.com"

print("Project number:", PROJECT_NUMBER)
print("Cloud Run service account:", SERVICE_ACCOUNT)


# In[ ]:


get_ipython().system('gcloud secrets add-iam-policy-binding power-automate-url    --member="serviceAccount:{SERVICE_ACCOUNT}"    --role="roles/secretmanager.secretAccessor"    --project={PROJECT_ID}')


# In[ ]:


get_ipython().run_line_magic('cd', '/content/drive/MyDrive/isic-flagship-project')

get_ipython().system('gcloud run deploy {SERVICE_NAME}    --source .    --region {REGION}    --allow-unauthenticated    --memory 4Gi    --cpu 1    --min-instances 1    --max-instances 3    --timeout 300    --port 8080    --cpu-boost    --set-secrets POWER_AUTOMATE_URL=power-automate-url:latest    --project {PROJECT_ID}')


# In[ ]:


import requests

CLOUD_RUN_URL = "https://isic-api-918647643601.europe-west2.run.app"

health = requests.get(f"{CLOUD_RUN_URL}/api/v1/health", timeout=30)
print("Health:", health.status_code)
print(health.json())

openapi = requests.get(f"{CLOUD_RUN_URL}/openapi.json", timeout=30).json()
paths = sorted(openapi.get("paths", {}).keys())

print("OpenAPI paths:")
for path in paths:
    print("-", path)

assert "/api/v1/predict" in paths
assert "/api/v1/health" in paths

assert "/api/v1/agent/health" not in paths
assert "/api/v1/agent/support" not in paths

schemas = openapi.get("components", {}).get("schemas", {})
assert "CopilotSupportRequest" not in schemas
assert "CopilotSupportResponse" not in schemas

print("Swagger cleanup check passed.")


# In[ ]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/api/main.py', '"""\nMain FastAPI application.\n"""\n\nfrom fastapi import FastAPI\nfrom fastapi.middleware.cors import CORSMiddleware\n\nfrom src.core.config import get_settings\nfrom src.api.routes import health_router, prediction_router\n\n\nsettings = get_settings()\n\ntags_metadata = [\n    {\n        "name": "prediction",\n        "description": "Upload a skin lesion image and receive a malignant-risk prediction.",\n    },\n    {\n        "name": "health",\n        "description": "Health check endpoints.",\n    },\n    {\n        "name": "general",\n        "description": "General API information.",\n    },\n]\n\napp = FastAPI(\n    title="ISIC Skin Lesion Platform API",\n    version=settings.API_VERSION,\n    description="ISIC Skin Lesion Detection API with image prediction endpoints.",\n    openapi_tags=tags_metadata,\n)\n\napp.add_middleware(\n    CORSMiddleware,\n    allow_origins=["*"],\n    allow_credentials=True,\n    allow_methods=["*"],\n    allow_headers=["*"],\n)\n\n\n@app.get("/", tags=["general"])\nasync def root():\n    return {\n        "status": "ok",\n        "service": "ISIC Skin Lesion Platform API",\n        "docs_url": "/docs",\n        "openapi_url": "/openapi.json",\n    }\n\n\napp.include_router(\n    prediction_router,\n    prefix="/api/v1",\n    tags=["prediction"],\n)\n\napp.include_router(\n    health_router,\n    prefix="/api/v1",\n    tags=["health"],\n)\n')

