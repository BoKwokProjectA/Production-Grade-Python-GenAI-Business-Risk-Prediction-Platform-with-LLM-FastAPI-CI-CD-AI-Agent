#!/usr/bin/env python
# coding: utf-8

# In[1]:


from google.colab import drive
drive.mount('/content/drive', force_remount=True)


# In[2]:


import os
from pathlib import Path

PROJECT_ROOT = "/content/drive/MyDrive/isic-flagship-project"
os.chdir(PROJECT_ROOT)
print("Working in:", os.getcwd())

prompts_dir = Path("prompts")
prompts_dir.mkdir(exist_ok=True)


# In[4]:


# v1_system_prompt.md - basic prompt for the support agent
v1_prompt = """You are the Skin Lesion Platform Support Agent.
You help users with technical questions about the ISIC prediction API and the project.

Rules:
- Only answer technical or usage questions about the platform.
- Never give medical advice or interpret any image as a diagnosis.
- Always be clear, polite and direct.
- If the question is medical, reply with the safety disclaimer and suggest seeing a doctor.
- Base your answers on the project documentation, README, and API specs only."""

with open("prompts/v1_system_prompt.md", "w") as f:
    f.write(v1_prompt)


# In[5]:


# v2_safety_prompt.md - added safety layer
v2_prompt = """You are the Skin Lesion Platform Support Agent (v2 - added safety layer).

Core rules:
- Answer ONLY technical questions about the API, how to upload images, what the probability means, troubleshooting, model architecture, or governance.
- If the user asks anything about their own skin lesion, diagnosis, treatment, or medical interpretation: immediately refuse and reply "I cannot provide medical advice or diagnose any skin condition. Please consult a qualified dermatologist."
- Always include the medical disclaimer when relevant.
- Never hallucinate features or capabilities that do not exist in the project.
- Keep answers short and factual."""

with open("prompts/v2_safety_prompt.md", "w") as f:
    f.write(v2_prompt)



# In[6]:


# prompt_changelog.md
changelog = """# Prompt Changelog

2026-05-15 - v2_safety_prompt.md
- Added stronger medical safety rules
- Clearer refusal language for diagnosis questions
- Linked to safety_tests.json for validation

2026-05-15 - v1_system_prompt.md
- Initial system prompt for technical support
- Basic grounding on project documentation

All changes are reviewed and tested against the agent_evaluation suite before use.
"""

with open("prompts/prompt_changelog.md", "w") as f:
    f.write(changelog)



# In[7]:


review_checklist = """# Prompt Review Checklist

- [ ] Does the prompt clearly forbid medical diagnosis/advice?
- [ ] Does it reference only real capabilities of the platform?
- [ ] Have I tested it against golden_cases.json?
- [ ] Have I run hallucination_tests.json and safety_tests.json?
- [ ] Is the new version added to prompt_changelog.md?
- [ ] Are evaluation results saved in agent_evaluation/results/?

Reviewed by: Bo Kwok
Date: 2026-05-15
"""

with open("prompts/prompt_review_checklist.md", "w") as f:
    f.write(review_checklist)


# In[8]:


import os
from pathlib import Path

PROJECT_ROOT = "/content/drive/MyDrive/isic-flagship-project"
os.chdir(PROJECT_ROOT)
print("Working in:", os.getcwd())

# Create the governance folder
governance_dir = Path("governance")
governance_dir.mkdir(exist_ok=True)


# In[9]:


action_tier = """# Action Tier Model

This table defines what the Skin Lesion Platform Support Agent is allowed to do.

| Action                              | Risk Level | Automation Allowed? | Notes |
|-------------------------------------|------------|---------------------|-------|
| Explain how the prediction endpoint works | Low       | Yes                 | Technical only |
| Explain probability score and model architecture | Low       | Yes                 | Factual only |
| Help with image upload or troubleshooting | Low       | Yes                 | Standard support |
| Answer general project or API questions | Low       | Yes                 | Grounded in documentation |
| Interpret any uploaded image medically | High      | No                  | Always refuse |
| Give diagnosis, treatment or medical advice | Prohibited | No               | Immediate refusal + doctor recommendation |
| Flag uncertain prediction for human review | Medium    | Yes (with review)   | Creates SharePoint item |

Reviewed: 2026-05-15
"""

with open("governance/action_tier_model.md", "w") as f:
    f.write(action_tier)


# In[10]:


classification = """# Classification Canon

classifying queries to the support agent:

- Technical / Usage questions → Low risk → Auto-answer
- Project architecture or governance questions → Low risk → Auto-answer
- Any question mentioning personal symptoms, diagnosis, treatment or "my lesion" → High risk → Refuse + medical disclaimer
- Requests for medical interpretation of images → Prohibited → Refuse
- Questions about model limitations or safety → Medium risk → Answer with clear disclaimer

This canon is used by the agent prompt and by the evaluation suite.

"""

with open("governance/classification_canon.md", "w") as f:
    f.write(classification)


# In[11]:


edge_cases = """# Edge Case Register

| Date       | Edge Case Description                          | How Handled                          | Status    |
|------------|------------------------------------------------|--------------------------------------|-----------|
| 2026-05-15 | User asks "Is this skin lesion cancer?"        | Refused with medical disclaimer      | Closed    |
| 2026-05-15 | User asks for treatment recommendation         | Refused + redirect to doctor         | Closed    |
| 2026-05-15 | User tries to upload non-image file            | API returns clear error              | Closed    |
| 2026-05-15 | User asks about model training data            | Answered factually (public Kaggle)   | Closed    |

New edge cases are added after testing with the evaluation suite.
"""

with open("governance/edge_case_register.md", "w") as f:
    f.write(edge_cases)


# In[12]:


security = """# Security Architecture

- All predictions and RAG queries run through the FastAPI backend
- No user data or uploaded images are stored permanently
- Input validation on image uploads (size, type)
- Structured error handling with no stack trace leakage
- Prompts and system instructions are version controlled
- Governance rules are enforced at prompt level and evaluation level
- Human review triggered for any high-risk action

This setup follows basic secure AI deployment practices.
"""

with open("governance/security_architecture.md", "w") as f:
    f.write(security)


# In[13]:


human_loop = """# Human-in-the-Loop Policy

When the agent detects high uncertainty or risk:
1. Prediction probability between 0.45 and 0.55 → flag for review
2. Any medical-related query → automatic refusal + escalation option
3. User feedback marked as negative → logged for review

Escalation creates a record in the prediction database and can trigger a simple notification workflow (future Power Automate integration).


"""

with open("governance/human_in_the_loop_policy.md", "w") as f:
    f.write(human_loop)


# In[14]:


safety_policy = """# Medical AI Safety Policy

This platform is for demonstration and technical research only.

- The system is NOT a medical device
- No prediction replaces professional medical advice
- All users must be told: consult a qualified dermatologist for any skin concern
- Medical interpretation of images is strictly prohibited
- Any attempt to use the system for diagnosis will be refused

This policy is enforced in every system prompt and safety test.

"""

with open("governance/medical_ai_safety_policy.md", "w") as f:
    f.write(safety_policy)


# In[15]:


governance_readme = """# Governance Artefacts

This folder contains the governance documents for the Skin Lesion Platform Support Agent.

It demonstrates the same practices expected in a professional AI team:
- Action Tier Model
- Classification Canon
- Edge Case Register
- Security Architecture
- Human-in-the-Loop Policy
- Medical AI Safety Policy

All documents are linked to the prompt versions and the agent evaluation suite.

"""

with open("governance/README.md", "w") as f:
    f.write(governance_readme)


# In[16]:


import os
from pathlib import Path

PROJECT_ROOT = "/content/drive/MyDrive/isic-flagship-project"
os.chdir(PROJECT_ROOT)
print("Working in:", os.getcwd())

pa_dir = Path("power_automate")
pa_dir.mkdir(exist_ok=True)


# In[17]:


readme = """# Prediction Risk Review Workflow (Power Automate Integration)

When the model returns a probability between 0.45 and 0.55, the FastAPI backend automatically calls the Power Automate flow for human review.

Flow name: ISIC Prediction Risk Review
"""

with open("power_automate/README.md", "w") as f:
    f.write(readme)


# In[18]:


workflow = """# Real Power Automate Flow Details

Trigger: When a HTTP request is received (POST)
Uncertain range: 0.45 - 0.55

Actions in the flow:
1. Parse JSON from FastAPI
2. Condition: probability between 0.45 and 0.55
3. Create item in SharePoint list "Prediction Reviews"
4. Send notification in Teams to reviewer
5. Wait for reviewer feedback
6. (Optional) Update back to database

This provides proper human-in-the-loop safety for uncertain predictions.
"""

with open("power_automate/workflow_details.md", "w") as f:
    f.write(workflow)


# In[19]:


get_ipython().run_cell_magic('writefile', 'src/services/prediction_service.py', '"""\nPrediction service with Power Automate human review trigger.\n"""\n\nimport io\nfrom datetime import datetime, timezone\n\nimport httpx\nfrom fastapi import UploadFile\nfrom PIL import Image\n\nfrom src.inference.ensemble_engine import ISICEnsembleEngine\nfrom src.core.config import get_settings\n\n\nclass PredictionService:\n    def __init__(self):\n        self.engine = ISICEnsembleEngine()\n        self.settings = get_settings()\n        self.engine.load_models()\n\n    async def predict(self, file: UploadFile):\n        image_bytes = await file.read()\n        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")\n\n        result = self.engine.predict(image)\n\n        probability = float(result["probability"])\n\n        if 0.45 <= probability <= 0.55:\n            await self._trigger_power_automate_review(result)\n\n        result["probability"] = probability\n        return result\n\n    async def _trigger_power_automate_review(self, result):\n        url = self.settings.POWER_AUTOMATE_URL\n\n        if not url:\n            return\n\n        payload = {\n            "isic_id": str(result.get("isic_id", "uploaded_image")),\n            "probability": float(result["probability"]),\n            "prediction": str(result["prediction"]),\n            "image_filename": str(result.get("image_filename", "unknown.jpg")),\n            "timestamp": datetime.now(timezone.utc).isoformat(),\n        }\n\n        try:\n            async with httpx.AsyncClient(timeout=15.0) as client:\n                await client.post(url, json=payload)\n        except Exception:\n            pass\n')


# In[20]:


import importlib
import src.services.prediction_service

importlib.reload(src.services.prediction_service)

from src.services.prediction_service import PredictionService


# In[21]:


get_ipython().run_cell_magic('writefile', 'src/core/config.py', '""" Core configuration """\n\nfrom pydantic_settings import BaseSettings\nfrom functools import lru_cache\n\nclass Settings(BaseSettings):\n    APP_NAME: str = "ISIC 2024 Skin Cancer Detection"\n    API_VERSION: str = "v1"\n    MODEL_VERSION: str = "2024-ensemble-v1"\n    DEBUG: bool = True\n    DATABASE_URL: str = "sqlite+aiosqlite:///./isic.db"\n    POWER_AUTOMATE_URL: str = ""\n    NGROK_AUTHTOKEN: str = ""\n    SECRET_KEY: str = "super-secret-key-change-in-production"\n\n    class Config:\n        env_file = ".env"\n        env_file_encoding = "utf-8"\n\n@lru_cache()\ndef get_settings() -> Settings:\n    return Settings()\n')


# In[22]:


from pathlib import Path
from google.colab import userdata
import os

PROJECT_ROOT = "/content/drive/MyDrive/isic-flagship-project"
env_file = Path(PROJECT_ROOT) / ".env"

power_automate_url = userdata.get("POWER_AUTOMATE_URL")

if not power_automate_url:
    raise ValueError("POWER_AUTOMATE_URL is missing from Colab Secrets")

os.environ["POWER_AUTOMATE_URL"] = power_automate_url

content = f"""APP_NAME=ISIC 2024 Skin Cancer Detection
API_VERSION=v1
MODEL_VERSION=2024-ensemble-v1
DEBUG=True
DATABASE_URL=sqlite+aiosqlite:///./isic.db
POWER_AUTOMATE_URL={power_automate_url}
NGROK_AUTHTOKEN=
SECRET_KEY=super-secret-key-change-in-production
"""

with open(env_file, "w") as f:
    f.write(content)

print("URL length:", len(power_automate_url))


# In[23]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/schemas/prediction.py', '"""\nPydantic schemas for API requests and responses\n"""\nfrom pydantic import BaseModel, Field\nfrom datetime import datetime\nfrom typing import Optional\n\nclass PredictionRequest(BaseModel):\n    isic_id: Optional[str] = None\n\nclass PredictionResponse(BaseModel):\n    isic_id: str\n    probability: float = Field(..., ge=0.0, le=1.0)\n    prediction: str\n    model_version: str\n    timestamp: datetime\n    review_triggered: bool = False\n\nclass HealthResponse(BaseModel):\n    status: str\n    model_version: str\n    api_version: str\n')


# In[24]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/api/routes.py', '"""\nAPI routes for skin lesion prediction.\n"""\nfrom fastapi import APIRouter, UploadFile, File, HTTPException\nfrom datetime import datetime\nfrom src.services.prediction_service import PredictionService\nfrom src.schemas.prediction import PredictionResponse\n\nprediction_service = PredictionService()\nprediction_router = APIRouter(prefix="/api/v1", tags=["prediction"])\n\n@prediction_router.post("/predict", response_model=PredictionResponse,\n    summary="Predict skin lesion risk",\n    description="""\n    Upload a dermoscopy image to get malignant risk prediction.\n\n    **Human-in-the-Loop Safety Feature:**\n    - If probability is between 0.45 and 0.55, the system automatically triggers\n      a human review via Power Automate.\n    - The field `review_triggered` will be `true` in such cases.\n    """)\nasync def predict_image(file: UploadFile = File(...)):\n    if not file.content_type or not file.content_type.startswith("image/"):\n        raise HTTPException(status_code=400, detail="File must be an image")\n\n    result = await prediction_service.predict(file)\n\n    return PredictionResponse(\n        isic_id=file.filename or "uploaded_image",\n        probability=result["probability"],\n        prediction=result["prediction"],\n        model_version=result.get("model_version", "2024-ensemble-2models"),\n        timestamp=datetime.utcnow(),\n        review_triggered=(0.45 <= result["probability"] <= 0.55)\n    )\n')


# In[26]:


get_ipython().system('gcloud services enable secretmanager.googleapis.com')


# In[27]:


from google.colab import auth, userdata
import os

auth.authenticate_user()

PROJECT_ID = "isic-flagship-project"

os.environ["PROJECT_ID"] = PROJECT_ID

get_ipython().system('gcloud config set project {PROJECT_ID}')
get_ipython().system('gcloud config list')


# In[ ]:


from google.colab import userdata
import os

power_automate_url = userdata.get("POWER_AUTOMATE_URL")

if not power_automate_url:
    raise ValueError("POWER_AUTOMATE_URL is missing from Colab Secrets")

os.environ["POWER_AUTOMATE_URL"] = power_automate_url

print("POWER_AUTOMATE_URL loaded from Colab Secrets")
print("URL length:", len(power_automate_url))


# In[ ]:


secret_file = "/tmp/power_automate_url.txt"

with open(secret_file, "w") as f:
    f.write(power_automate_url)

get_ipython().system('gcloud secrets create power-automate-url    --replication-policy="automatic"    --data-file={secret_file}    --project={PROJECT_ID}    || gcloud secrets versions add power-automate-url    --data-file={secret_file}    --project={PROJECT_ID}')

