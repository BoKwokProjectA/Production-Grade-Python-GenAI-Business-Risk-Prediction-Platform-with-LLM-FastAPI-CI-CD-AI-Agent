# Production Grade Python GenAI Business Risk Prediction Platform with LLM applications, FastAPI, RAG Assistant, CI, CD, Real Time ML Inference, AI Agent, AI Automation, DevOps and MLOps Oriented Deployment: Post Graduation Project 

[![CI](https://github.com/BoKwokProjectA/Production-Grade-AI-Medical-Image-Risk-Prediction-Platform-FastAPI-Docker-RAG-SQLite-Cloud/actions/workflows/ci.yml/badge.svg)](https://github.com/BoKwokProjectA/Production-Grade-AI-Medical-Image-Risk-Prediction-Platform-FastAPI-Docker-RAG-SQLite-Cloud/actions/workflows/ci.yml)
[![Docker Build Smoke Test](https://github.com/BoKwokProjectA/Production-Grade-AI-Medical-Image-Risk-Prediction-Platform-FastAPI-Docker-RAG-SQLite-Cloud/actions/workflows/docker-build.yml/badge.svg)](https://github.com/BoKwokProjectA/Production-Grade-AI-Medical-Image-Risk-Prediction-Platform-FastAPI-Docker-RAG-SQLite-Cloud/actions/workflows/docker-build.yml)
[![Deploy to Cloud Run](https://github.com/BoKwokProjectA/Production-Grade-AI-Medical-Image-Risk-Prediction-Platform-FastAPI-Docker-RAG-SQLite-Cloud/actions/workflows/deploy-cloud-run.yml/badge.svg)](https://github.com/BoKwokProjectA/Production-Grade-AI-Medical-Image-Risk-Prediction-Platform-FastAPI-Docker-RAG-SQLite-Cloud/actions/workflows/deploy-cloud-run.yml)

## Overview

This project turns a risk detection research workflow into a deployed, production-style machine learning API, reflecting how modern businesses use risk prediction systems.

Users can upload an image through a FastAPI backend and receive a risk prediction from a two-model vision ensemble using ConvNeXt and EVA-02. The API is containerized with Docker and deployed primarily on Azure Container Apps, with the previous Google Cloud Run deployment retained as backup and rollback evidence. It includes interactive Swagger documentation, health checks, structured logging, clean backend architecture, and a retrieval-based RAG assistant for project/codebase Q&A.

This repository is presented as a job-application portfolio project for machine learning engineering, AI engineering, automation engineering, backend engineering, and MLOps-oriented roles. It demonstrates the ability to move from notebook experimentation to a deployed API, design production-style software architecture, package an ML system with Docker, connect the backend to a working Power Platform/Copilot Studio workflow, deploy to cloud infrastructure, and document safety and governance decisions clearly.

The goal of this project is not only to build a model inference endpoint, but to demonstrate how machine learning research code can be transformed into a real backend system that is easier to deploy, document, monitor, and extend.

## Live Demo

**Full-stack portfolio demo**

Frontend Portfolio App: https://production-grade-python-gen-ai-busi.vercel.app/

**Primary backend deployment: Azure Container Apps**

Live API: https://isic-api-azure.livelybeach-7ed547b8.uksouth.azurecontainerapps.io   
Interactive Swagger Docs: https://isic-api-azure.livelybeach-7ed547b8.uksouth.azurecontainerapps.io/docs   
OpenAPI Schema: https://isic-api-azure.livelybeach-7ed547b8.uksouth.azurecontainerapps.io/openapi.json   
Health Check: https://isic-api-azure.livelybeach-7ed547b8.uksouth.azurecontainerapps.io/api/v1/health   

**Previous / backup backend deployment: Google Cloud Run**

Backup Live API: https://isic-api-918647643601.europe-west2.run.app   
Backup Swagger Docs: https://isic-api-918647643601.europe-west2.run.app/docs    
Backup OpenAPI Schema: https://isic-api-918647643601.europe-west2.run.app/openapi.json    
Backup Health Check: https://isic-api-918647643601.europe-west2.run.app/api/v1/health    


<img width="1600" height="706" alt="1" src="https://github.com/user-attachments/assets/81975874-c9f3-491c-a41e-265be10b2ee3" />
<img width="1600" height="701" alt="2" src="https://github.com/user-attachments/assets/770165ea-d25e-4465-9ea5-e428a63267a6" />
<img width="1600" height="698" alt="3" src="https://github.com/user-attachments/assets/5ed0d5d9-79e6-490c-a8ba-f7f548922d63" />

Deployment note: the primary backend is deployed with Docker on Azure Container Apps. The previous Google Cloud Run deployment is retained as backup, rollback evidence, and a secondary cloud deployment example.

## Frontend Portfolio App

A Version 2 portfolio frontend has been added using **React, TypeScript, Vite, Tailwind CSS, and Vercel**.

The frontend presents the deployed FastAPI backend as a business-facing AI risk prediction platform. It connects to the live backend through `VITE_API_BASE_URL` and demonstrates a complete full-stack workflow from browser UI to production API response.

**Live Frontend:** https://production-grade-python-gen-ai-busi.vercel.app/
**Frontend Source:** `portfolio-frontend-v2/`  
**Backend API:** https://isic-api-azure.livelybeach-7ed547b8.uksouth.azurecontainerapps.io  
**Swagger Docs:** https://isic-api-azure.livelybeach-7ed547b8.uksouth.azurecontainerapps.io/docs  

Frontend capabilities include:

- Responsive Tailwind CSS landing page
- Image upload and risk scoring workflow
- Backend health check using `GET /api/v1/health`
- Prediction/risk scoring call using `POST /api/v1/predict`
- Typed TypeScript API response models
- Loading state during API calls
- Error handling for no file, unsupported upload, backend/API failure, and network failure
- Clear result display with uploaded file name, risk label, probability score, model version, and timestamp
- Safety and governance disclaimer
- Vercel deployment with environment-based backend configuration

The frontend does not store private secrets. The deployed backend URL is configured through:

VITE_API_BASE_URL=https://isic-api-azure.livelybeach-7ed547b8.uksouth.azurecontainerapps.io

## Project Highlights

- Added a React, TypeScript, Vite, and Tailwind CSS frontend deployed on Vercel.
- Built a business-facing AI risk prediction platform UI connected to the deployed FastAPI backend.
- Implemented frontend image upload, backend health monitoring, typed API response handling, loading states, and error handling.
- Configured the frontend with `VITE_API_BASE_URL` so the deployed Vercel app can call the Azure Container Apps backend without exposing private secrets.
- Built upon the 1st/2nd place winning solution concept of a Kaggle Challenge
- Transformed a Kaggle / notebook-based workflow into a production-oriented backend system
- Deployed a working FastAPI API with Docker on Azure Container Apps, with the previous Google Cloud Run deployment retained as backup.
- Added Azure Container Apps as the primary live deployment while keeping the existing Google Cloud Run deployment intact as backup / rollback evidence.
- Deployed the Dockerized FastAPI API to Azure Container Apps in UK South using Azure Container Registry, managed identity-based ACR image pull, Log Analytics and scale-to-zero cost controls.
- Added a GitHub Actions CI/CD pipeline with Ruff linting, Black formatting checks, pytest endpoint tests, Docker image build smoke testing, and automated Google Cloud Run source deployment with a live post-deployment check.
- Integrated a two-model production inference backend using ConvNeXt + EVA-02
- Added real image upload support for risk prediction
- Built a retrieval-based RAG assistant for project/codebase technical Q&A
- Added clean architecture, structured logging, checks, Pydantic schemas, and environment-based configuration
- Configured Cloud Run with warm instance support using `--min-instances 1` for live demo readiness
- Demonstrates the full ML application lifecycle: notebook experimentation, real-time inference API design, Docker packaging, cloud deployment, Power Automate workflow integration, API documentation, observability, and safety boundaries
- Added prompt/versioning, evaluation, governance, and Power Automate workflow artefacts for safer AI assistant and automation development
- Integrated a working Power Automate workflow with the Dockerized FastAPI backend to demonstrate practical AI automation around the deployed API
- Added a Python 3.11 slim Dockerfile, pinned deployment requirements, .dockerignore, Google Cloud project configuration, Secret Manager IAM binding, and a reproducible Cloud Run deploy command.
- Added a Copilot Studio support-agent package with OpenAPI 2.0 custom connector, technical support topics, SharePoint knowledge pack packaging, manual test cases, and portfolio evidence checklist.
- Activated a Microsoft Copilot Studio technical support agent inside the live demo website, enabling users to ask platform-support questions through an embedded web chat experience.
- Added Microsoft SharePoint as a structured knowledge-document source for the Copilot Studio support agent, using converted PDF knowledge documents for project grounding, governance references, safety boundaries, and technical support Q&A.

## Project Structure

```text
src/
├── api/                  # FastAPI routes & main app
├── core/                 # Config, logger, settings
├── db/                   # SQLAlchemy models
├── inference/            # Core ML inference engine
├── rag/                  # RAG Technical Assistant
├── repositories/         # Database repository layer
├── schemas/              # Pydantic request/response models
├── services/             # Business logic
└── __init__.py

copilot_studio/
├── openapi/              # OpenAPI custom connector definition for Copilot Studio
├── topics/               # Copilot Studio support topic markdown files
└── sharepoint_knowledge_pack/ # Files prepared for SharePoint knowledge upload

portfolio-frontend-v2/
├── src/
│   ├── components/       # Reusable React UI components
│   ├── lib/              # API client and frontend constants
│   ├── types/            # TypeScript API response types
│   ├── App.tsx           # Main frontend layout
│   ├── main.tsx          # React entry point
│   └── index.css         # Tailwind CSS entry styles
├── index.html
├── package.json
├── vite.config.ts
└── .env.example


notebooks/                # Development & refactoring notebooks
configs/                  # Configuration files
data/                     # Data artifacts / local data references
logs/                     # Application logs
docker/                   # Docker-related deployment assets
prompts/                  # Prompt versions and review checklist for assistant safety
governance/               # AI safety and governance documentation
agent_evaluation/         # Golden cases, hallucination checks, and safety tests
power_automate/               # Power Automate workflow notes and integration assets
```

## Tech Stack

**Backend:** FastAPI, Uvicorn, Pydantic
**Frontend:** React, TypeScript, Vite, Tailwind CSS  
**Frontend Deployment:** Vercel  
**ML:** PyTorch, TorchVision, Timm, scikit-learn  
**Vision Models:** ConvNeXt, EVA-02  
**RAG:** LangChain, FAISS, Sentence Transformers  
**Database Layer:** SQLAlchemy, SQLite-ready repository layer  
**Deployment:** Docker, Azure Container Apps, Azure Container Registry, Google Cloud Run, Google Cloud Build  
**AI Automation:** Power Automate workflow integrated with the Dockerized FastAPI backend
**Microsoft 365 Knowledge Source:** SharePoint document library used to store Copilot Studio knowledge documents as PDF-based grounding material  
**Logging & Config:** structlog, Pydantic Settings  
**Notebook Development:** Google Colab  
**AI Safety / Evaluation Artefacts:** Prompt changelog, prompt review checklist, golden cases, hallucination tests, safety tests, governance documents

## Key Features

### Frontend Portfolio Platform

**React + TypeScript Frontend:** Adds a modern portfolio-quality frontend using React, TypeScript, Vite, and Tailwind CSS.

**Business-Facing Risk Platform UI:** Presents the system as an AI risk prediction platform with professional wording suitable for job applications and technical demos.

**Image Upload Workflow:** Allows users to select a supported image file and submit it to the deployed backend using multipart form-data.

**Typed API Client:** Uses TypeScript interfaces for health check and prediction/risk scoring responses.

**Backend Health Monitoring:** Calls `GET /api/v1/health` from the browser and displays backend status, API version, model version, and service information.

**Risk Scoring Result Display:** Shows uploaded file name, backend file ID, risk label, probability score, model version, and timestamp.

**Loading and Error States:** Handles no-file validation, unsupported file type validation, backend errors, and network failures.

**Environment-Based Backend URL:** Uses `VITE_API_BASE_URL` so the same frontend can point to Azure Container Apps, Google Cloud Run, or another deployed backend.

**Vercel Deployment:** Deployed as a Vercel frontend project with `portfolio-frontend-v2` as the root directory.

### Core ML Capabilities

**Two-Model Vision Ensemble:** Uses `convnext_small` and `eva02_small_patch14_336` through PyTorch + Timm for deployed image inference.

**Model-Specific Image Transforms:** Uses model-specific resize/crop pipelines such as 384px preprocessing for ConvNeXt and 336px preprocessing for EVA-02.

**Lazy Model Loading:** Models are loaded once and reused for inference through a `models_loaded` flag.

**Device-Aware Inference:** Automatically selects CUDA when available and CPU otherwise.

**Mean Ensemble Prediction:** Combines model probabilities through simple ensemble averaging.

**Real Image Upload Inference Endpoint:** Upload a supported image and receive a binary model risk score and classification result.

**Probability-Based Classification:** Converts positive-class probability into low-risk/high-risk classification labels using the backend prediction flow.

### Prediction Logic

The API performs image inference using a two-model ensemble: ConvNeXt Small + EVA-02 Small.

Each model processes the uploaded image independently.
Both models produce a score for the configured positive-risk class.
The final model score is calculated by averaging the two outputs.
Demonstration classification rule:
Score < 0.5 → lower_risk
Score >= 0.5 → higher_risk

The threshold is included for demonstration purposes and can be configured for other business risk-classification scenarios. The output is a model-generated score rather than a verified real-world decision.

### Production Backend

**FastAPI with Clean Architecture:** Layered structure using API routes, services, repositories, schemas, models, inference, RAG, and core configuration.

**Async Image Processing:** Handles image uploads with validation before inference.

**Pydantic v2 Schemas:** Strong type validation and automatic OpenAPI documentation.

**Structured Logging:** Application logging using `structlog` JSON rendering.

**Application Lifespan Hooks:** Logs startup and shutdown events through FastAPI lifespan management.

**CORS Middleware:** Enables cross-origin usage for web clients, demos, and frontend integration.

**Image Upload Validation:** Rejects non-image uploads with a meaningful `400` response.

**Typed Prediction Response:** Returns `isic_id`, `probability`, `prediction`, `model_version`, and `timestamp`.

**Config Caching:** Uses `@lru_cache()` for efficient settings loading.

**Environment Configuration:** Uses `.env` with fields such as `APP_NAME`, `API_VERSION`, `MODEL_VERSION`, `DEBUG`, `DATABASE_URL`, and `SECRET_KEY`.

**Copilot Support Schemas:** CopilotSupportRequest validates question, conversation_id, and user_role; CopilotSupportResponse returns answer, intent, risk_level, automation_allowed, escalation_required, sources, and safety_note.

**Support Service Intent Routing:** Copilot Support Service classifies support requests into technical intent categories such as `api_support`, `image_upload_support`, `failed_upload_support`, `prediction_explanation`, `governance`, `general_platform_support`, and `medical_advice`. Requests requiring professional domain judgement are treated as restricted and redirected to an appropriately qualified professional rather than answered or actioned automatically.

### Intelligent RAG Assistant

**Project-Aware Retrieval Assistant:** Retrieves relevant project source-code context for technical Q&A.

**Vector Search:** Uses FAISS with Sentence Transformers embeddings.

**Codebase Indexing:** Indexes Python files from `src/**/*.py` plus a short project summary.

**Chat Endpoint:** `/api/v1/chat` accepts a question and returns retrieved project context.

### Microsoft Copilot Studio AI Agent, Demo Website Integration, Power Platform Connector, and Safety Behaviour

The Copilot Studio notebook creates a technical-support agent for the AI Risk Intelligence Platform. The agent can explain API usage, image upload steps, probability scores, failed uploads, governance, and restricted-use boundaries. It must not make professional judgements, interpret user-submitted content as authoritative evidence, or trigger consequential actions without human review.

The Copilot Studio agent is also activated in the live demo website as an embedded technical-support chat experience. The agent is scoped to project and platform support only. It can explain API usage, image upload requirements, prediction response fields, failed upload troubleshooting, workflow behaviour, governance documents, and safety limitations.

The agent does not provide professional advice, make consequential decisions, or replace qualified human review. Restricted professional-advice requests are declined and redirected to an appropriately qualified professional.

**SharePoint Knowledge Source:** The Copilot Studio support agent uses a Microsoft SharePoint document library as its knowledge source. Project support and governance documents were converted into PDF format and uploaded to SharePoint so the agent can ground answers in maintained documentation about API usage, image uploads, probability scores, failed-upload troubleshooting, action tiers, human-in-the-loop review, security architecture, and restricted-use boundaries.

The SharePoint knowledge source is used only for technical and operational platform support. It is not used to provide medical diagnosis, treatment advice, or lesion interpretation.

The updated project notebooks introduce a technical AI agent, Power Automate workflow integration, and supporting artefacts for safer AI-assistant development. These are included as portfolio evidence of responsible AI engineering and practical automation integration.
**AI Agent:** Provides technical support around the platform, API behaviour, upload flow, prediction response format, governance process, and safety limitations.
**Power Automate Integration:** Connects a working Power Automate workflow to the Dockerized FastAPI backend, showing how the deployed API can be used inside a low-code automation flow.
**Prompt Versioning:** Includes system prompt versions, safety-focused prompt updates, a prompt changelog, and a review checklist.

**Safety-Focused Assistant Rules:** Defines boundaries for technical support, including refusing medical diagnosis, treatment advice, or image interpretation requests.

**Evaluation Suite:** Includes golden cases for expected technical answers, hallucination checks, regression-style tests, and safety tests.

**Governance Documentation:** Includes an action tier model, medical AI safety policy, human-in-the-loop policy, security architecture notes, edge case register, and classification canon.

**Medical safety rule:** if the user asks for diagnosis, treatment, or lesion interpretation, the agent refuses and redirects the user to a qualified clinician while still offering technical platform information.

These artefacts show how the project combines safer assistant behaviour, evaluation gates, governance practices, and a working automation workflow without presenting the system as a medical decision-making tool.

### Production & Observability

**SQLite-Ready Persistence Layer:** SQLAlchemy model and repository structure are prepared for future prediction history storage.

**Repository Pattern:** Encapsulates future database write logic in `PredictionRepository`.

**Error Handling:** Includes validation and meaningful API errors for unsupported uploads and service-level failures.

**Health Check Support:** Health endpoint is available for deployment checks and uptime monitoring.

**Docker Support:** Fully containerized for cloud deployment.

**Google Cloud Run Backup Deployment:** The previous Google Cloud Run deployment remains available as backup and rollback evidence.

**Google Cloud Build Source Deployment:** Uses `gcloud run deploy --source .` deployment workflow.

**Azure Container Apps Deployment:** Added a second cloud deployment target using Azure Container Apps in UK South.

**Azure Container Registry:** Stores the Docker image used by Azure Container Apps.

**Managed Identity Image Pull:** Azure Container Apps uses a user-assigned managed identity with `AcrPull` permission to pull the image from Azure Container Registry without storing registry passwords.

**Azure Log Analytics:** Container Apps logs are connected to a Log Analytics workspace for deployment debugging and runtime observability.

**Scale-to-Zero Cost Control:** Azure Container Apps is configured with `min-replicas 0` and `max-replicas 1` to control pay-as-you-go cost during portfolio demo usage.

**Warm Instance Setup:** Cloud Run configured with `--min-instances 1` for live demo readiness and reduced cold-start impact.

**JSON Structured Logs:** `structlog` is configured with JSON rendering for production log aggregation.

**Startup/Shutdown Logging:** Application lifecycle events are recorded for easier debugging.

### Developer Experience

**Modular Codebase:** Separated API, service, inference, RAG, schema, config, and repository layers.

**Notebook-to-Production Workflow:** Refactored setup, inference, backend, RAG, ensemble, and deployment work from notebooks into a deployable project.

**Deployment Ready:** Containerized for Docker and Google Cloud Run.

**Full ML Application Lifecycle:** Documents how the work moves from notebook experimentation into a deployed API with clear review points across model inference, backend architecture, deployment, automation integration, monitoring readiness, and safety.


## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Root endpoint confirming the API is running |
| GET | `/docs` | Interactive Swagger/OpenAPI documentation |
| GET | `/openapi.json` | OpenAPI schema |
| GET | `/api/v1/health` | Health check with API and model version |
| POST | `/api/v1/predict` | Upload a skin lesion image and receive prediction results |
| POST | `/api/v1/chat` | Ask the RAG assistant about the project/codebase |
| GET | `/api/v1/agent/health` | Health check for the Copilot Studio support-agent connector |
| POST | `/api/v1/agent/support` | Custom connector endpoint used by Copilot Studio to answer technical support questions |

## Prediction Response Example

```json
{
  "isic_id": "uploaded_image.jpg",
  "probability": 0.7321,
  "prediction": "malignant",
  "model_version": "2024-ensemble-2models",
  "timestamp": "2026-01-01T12:00:00"
}
```

## RAG Assistant Example

Request:

```json
{
  "question": "How does the ensemble inference engine work?"
}
```

Response:

```json
{
  "answer": "Context from project: ... Question: How does the ensemble inference engine work?"
}
```

## Microsoft Copilot Studio AI Agent Example

Request:
```json
{
  "question": "Is this lesion cancer?",
  "conversation_id": "copilot-live-test-001",
  "user_role": "user"
}
```

Response:
```json
{
  "answer": "I can help with technical questions about the Skin Lesion Platform... I cannot interpret a lesion, confirm whether it is cancer, decide whether it is benign or malignant, or recommend treatment. For medical concerns, please speak with a qualified clinician.",
  "intent": "medical_advice",
  "risk_level": "Prohibited",
  "automation_allowed": false,
  "escalation_required": true,
  "sources": [
    "governance/medical_ai_safety_policy.md",
    "governance/action_tier_model.md",
    "governance/human_in_the_loop_policy.md"
  ],
  "safety_note": "Medical diagnosis, lesion interpretation, and treatment advice are outside the agent's allowed scope."
}
```

## Docker

The project is containerized with Docker and deployed successfully on Google Cloud Run. The Dockerfile runs the FastAPI app on port `8080`.

Reference Docker commands:

```bash
docker build -t isic-flagship .
docker run -p 8000:8080 isic-flagship
```

Container startup command:

```bash
uvicorn src.api.main:app --host 0.0.0.0 --port ${PORT:-8080}
```

Requirements include FastAPI 0.115.2, Uvicorn 0.32.0, Pydantic 2.9.2, SQLAlchemy 2.0.35, pandas 2.2.2, numpy 1.26.4, pillow 10.4.0, timm 1.0.11, LightGBM 4.5.0, CatBoost 1.2.7, XGBoost 2.1.1, scikit-learn 1.5.2, LangChain 0.3.4, FAISS CPU 1.8.0.post1, Sentence Transformers 3.1.1, python-multipart 0.0.9, httpx 0.27.2, and structlog 24.4.0.

For Google Cloud Run, the container uses the platform-provided `PORT` environment variable. The deployment can be kept warm with `--min-instances 1` for live demo readiness.



## Power Automate Workflow and Copilot Studio Integration

The project includes a Power Platform custom connector and Copilot Studio technical support-agent integration connected to the Dockerized FastAPI backend. The backend also accepts a `POWER_AUTOMATE_URL` secret. In Google Cloud Run this can be configured through Google Secret Manager, while in Azure Container Apps it is configured as a Container Apps secret. The real webhook URL is not committed to GitHub.
The Copilot Studio agent is also connected to a SharePoint knowledge source containing PDF versions of the project support and governance documents. This gives the agent a maintained document source for technical support answers while keeping the medical safety boundary explicit.

The automation layer is presented as practical AI workflow automation around the backend. It does not automate medical diagnosis, treatment advice, or clinical decision-making.

**Copilot Studio setup:** create an agent named Skin Lesion Platform AI Agent, describe it as technical support only, add the knowledge source, import the custom connector, add the support action, add the six support topics, run the manual tests, and publish only after safety checks pass.

The Copilot Studio agent has been activated in the live demo website, allowing users to interact with the support agent through an embedded web chat interface. This demonstrates a working end-user AI support layer on top of the deployed FastAPI backend and Power Platform integration.

## Google Cloud Run Deployment

The API is deployed on Google Cloud Run using Docker and Google Cloud Build source deployment.

**Cloud Platform:** Google Cloud Run  
**Build System:** Google Cloud Build via `gcloud run deploy --source .`  
**Runtime Port:** `8080`  
**Warm Instance Setup:** `--min-instances 1` for live demo readiness  
**Public Access:** `--allow-unauthenticated`  
**API Docs:** Available through FastAPI Swagger UI at `/docs`

Example deployment command from the notebook workflow:

```bash
gcloud run deploy isic-api \
  --source . \
  --region europe-west2 \
  --allow-unauthenticated \
  --memory 4Gi \
  --cpu 1 \
  --min-instances 1 \
  --max-instances 3 \
  --timeout 300 \
  --port 8080 \
  --cpu-boost \
  --set-secrets POWER_AUTOMATE_URL=power-automate-url:latest \
  --project isic-flagship-project
```

## Azure Container Apps Deployment

The API is also deployed to Azure Container Apps as the primary live portfolio demo deployment.

This Azure deployment was added safely without deleting or replacing the existing Google Cloud Run deployment. Google Cloud Run remains available as backup and rollback evidence.

**Azure platform:** Azure Container Apps
**Azure region:** UK South
**Container registry:** Azure Container Registry
**Image:** `isicapiacrhp7lku.azurecr.io/isic-api:azure-demo-v2`
**Runtime port:** `8080`
**Public access:** External HTTPS ingress
**CPU / memory:** 2 vCPU / 4Gi
**Scale setting:** min replicas `0`, max replicas `1`
**Cost-control approach:** Consumption-style scale-to-zero configuration for low-cost portfolio testing
**Backup deployment:** Google Cloud Run remains available as rollback evidence

Example Azure deployment commands:

```bash
LOCATION="uksouth"
RG="rg-isic-aca-demo-uks"
ACR_NAME="isicapiacrhp7lku"
APP_NAME="isic-api-azure"
ENV_NAME="aca-env-isic-demo-uks"
IDENTITY_NAME="id-isic-aca-pull"
IMAGE_NAME="isic-api"
IMAGE_TAG="azure-demo-v2"

ACR_LOGIN_SERVER=$(az acr show \
  --name "$ACR_NAME" \
  --resource-group "$RG" \
  --query loginServer \
  -o tsv)

IDENTITY_ID=$(az identity show \
  --name "$IDENTITY_NAME" \
  --resource-group "$RG" \
  --query id \
  -o tsv)

FULL_IMAGE_NAME="$ACR_LOGIN_SERVER/$IMAGE_NAME:$IMAGE_TAG"

az containerapp update \
  --name "$APP_NAME" \
  --resource-group "$RG" \
  --image "$FULL_IMAGE_NAME" \
  --cpu 2.0 \
  --memory 4.0Gi \
  --min-replicas 0 \
  --max-replicas 1
```

Secrets such as `SECRET_KEY` and `POWER_AUTOMATE_URL` are configured through Azure Container Apps secrets and are not committed to GitHub.

### Azure endpoint checks

The Azure deployment was tested through:

```text
/
 /docs
/openapi.json
/api/v1/health
/api/v1/predict
```

Deployment evidence is stored under:

```text
deployment/azure/
```

### Cost-control note

The Azure deployment uses `min-replicas 0` and `max-replicas 1` to keep pay-as-you-go costs low. This allows the app to scale to zero when unused.

Because this API uses ML/RAG dependencies, the first request after scale-to-zero may be slower due to cold start. For short live demo periods, the app can temporarily be set to `min-replicas 1`, then returned to `min-replicas 0` after testing.

### Rollback note

The previous Google Cloud Run deployment remains intact.

If Azure fails, the README/demo links can be switched back to the Cloud Run deployment:

```text
https://isic-api-918647643601.europe-west2.run.app
```

GCP should not be deleted until a later migration phase.

## Vercel Frontend Deployment

The Version 2 frontend is deployed on Vercel from the `portfolio-frontend-v2/` directory.

Vercel configuration:

```text
Root Directory: portfolio-frontend-v2
Framework Preset: Vite
Build Command: npm run build
Output Directory: dist
Install Command: npm install
```

Required frontend environment variable:

```env
VITE_API_BASE_URL=https://isic-api-azure.livelybeach-7ed547b8.uksouth.azurecontainerapps.io
```

The frontend does not contain private secrets. Only public frontend-safe `VITE_` variables are used.

The deployed frontend calls:

```text
GET /api/v1/health
POST /api/v1/predict
```

The Azure Container Apps backend is used as the primary API target, while the Google Cloud Run deployment remains available as backup evidence.

## CI/CD with GitHub Actions

This repository includes a basic portfolio-grade CI/CD pipeline using GitHub Actions.

The CI workflow runs on push and pull request events. It installs dependencies, runs Ruff linting, checks Black formatting, and executes pytest tests using dummy environment variables so CI does not call real OpenAI APIs, Power Automate webhooks, or production secrets.

The Docker workflow builds the FastAPI Docker image, starts the container inside GitHub Actions, and smoke-tests the `/api/v1/health` endpoint to confirm the container can run successfully.

The deployment workflow deploys automatically to Google Cloud Run after the Docker smoke test succeeds on `main`. It uses Cloud Run source deployment:

```bash
gcloud run deploy isic-api --source .
```

This means the GitHub Actions workflow does not explicitly build, tag, or publish a Docker image to Artifact Registry. Google Cloud Build builds the service from source for Cloud Run.

For cost control, the automated deployment is configured with `--min-instances 0` and `--max-instances 1`. The workflow finishes with a live post-deployment health check against `/api/v1/health`.

CI test coverage includes:

* FastAPI app import test
* `/api/v1/health` endpoint test
* Invalid image upload rejection test
* Basic RAG assistant endpoint test
* Copilot/support-agent medical safety refusal test

This CI/CD setup supports a valid portfolio claim of automated testing, Docker smoke testing, and Cloud Run deployment for a FastAPI AI inference API. The project remains a portfolio AI engineering demo and is not a clinical diagnostic product, not a medical device, and not intended for diagnosis, treatment, or clinical decision-making.


## Environment Variables

Example `.env` / `.env.example`:

```env
APP_NAME=ISIC2024-Flagship
API_VERSION=v1
MODEL_VERSION=2024-ensemble-2models
DEBUG=False
DATABASE_URL=sqlite:///./isic.db
SECRET_KEY=change-this-in-google-cloud-run
POWER_AUTOMATE_URL=your-power-automate-webhook-url
```

## Copilot Studio Knowledge Sources and Topics

The Copilot Studio notebook creates these six topic files under copilot_studio/topics/: upload_image.md, prediction_endpoint.md, probability.md, failed_upload.md, governance.md, and medical_safety.md.

Required/target knowledge documents include README.md, prompts/v1_system_prompt.md, prompts/v2_safety_prompt.md, prompts/prompt_changelog.md, governance/action_tier_model.md, governance/classification_canon.md, governance/human_in_the_loop_policy.md, governance/medical_ai_safety_policy.md, and governance/security_architecture.md.

The knowledge pack packaging process copies README, Copilot Studio setup/topic files, prompt files, and governance files into `copilot_studio/sharepoint_knowledge_pack/`. These documents are then converted or exported into PDF format where needed and uploaded to a SharePoint document library for use as Copilot Studio knowledge sources.

The SharePoint knowledge documents include platform-support material for:

- Prediction endpoint usage
- Image upload steps and failed-upload troubleshooting
- Probability score explanation
- Governance and action tiers
- Human-in-the-loop review policy
- Medical AI safety policy
- Security architecture
- Prompt versioning and safety rules

## Evaluation and Safety Artefacts

The updated notebook workflow includes evaluation and governance files that support responsible AI development:

```text
prompts/
├── v1_system_prompt.md
├── v2_safety_prompt.md
├── prompt_changelog.md
└── prompt_review_checklist.md

agent_evaluation/
├── golden_cases.json
├── hallucination_tests.json
├── safety_tests.json
└── results/

governance/
├── action_tier_model.md
├── classification_canon.md
├── edge_case_register.md
├── human_in_the_loop_policy.md
├── medical_ai_safety_policy.md
├── security_architecture.md
└── README.md
```

These files demonstrate that the project considers:

- Medical AI safety boundaries
- Technical-support-only assistant behaviour
- Refusal behaviour for diagnosis or treatment questions
- Golden-case testing for expected answers
- Hallucination and safety testing
- Prompt review and changelog discipline
- Governance documentation suitable for professional AI workflows
- Power Automate workflow integration is presented as a working automation layer connected to the Dockerized backend. The AI agent remains scoped to technical support and safety-aware platform guidance, not medical diagnosis or treatment advice.

## Achievements

- Built and deployed a portfolio-grade React, TypeScript, Vite, and Tailwind CSS frontend on Vercel.
- Connected the Vercel frontend to the deployed FastAPI backend through environment-based configuration.
- Implemented a full-stack browser-to-API workflow with image upload, backend health check, loading state, error handling, and typed result rendering.
- Repositioned the frontend as a business-facing AI risk prediction platform while retaining safety and governance boundaries.
- Transformed an ISIC 2024-inspired notebook workflow into a deployed ML inference API
- Deployed a working FastAPI backend on Google Cloud Run with Docker
- Added Azure Container Apps deployment as the primary live demo while keeping Google Cloud Run intact as backup / rollback evidence.
- Used Azure Container Registry, managed identity-based image pull, Azure Log Analytics, and Container Apps scale controls for a low-cost Azure deployment.
- Implemented GitHub Actions CI/CD with Ruff, Black, pytest, Docker container smoke testing, and automated Google Cloud Run source deployment.
- Integrated ConvNeXt + EVA-02 as the implemented production model ensemble
- Added real image upload inference and interactive Swagger/OpenAPI documentation
- Added a retrieval-based RAG assistant using FAISS and Sentence Transformers
- Structured the project with modular API, service, inference, RAG, schema, config, logging, and SQLite-ready repository layers
- Demonstrated an end-to-end notebook-to-production workflow suitable for machine learning engineering and MLOps-oriented job applications
- Added prompt-versioning, safety-test, and governance artefacts to show responsible AI engineering practice
- Integrated a working Power Automate workflow with the Dockerized FastAPI backend to demonstrate practical AI automation
- Added technical AI support agent endpoints with safety-aware responses for platform, API, workflow, and governance questions
- Added a Copilot Studio AI agent package with OpenAPI custom connector, technical support topics, knowledge-pack packaging, and setup/evidence checklists.
- Added Validated support-agent health and safety refusal behaviour against the live Cloud Run endpoint.
- Activated the Copilot Studio support agent inside the live demo website, demonstrating a working end-user AI support experience connected to the deployed platform.
- Added a SharePoint-based Copilot Studio knowledge source using PDF versions of project documentation, governance files, safety policies, and support-topic material.


## Safety and Governance Disclaimer

This project is an educational and job-application portfolio implementation of a full-stack AI risk prediction platform.

It is not a regulated product, clinical decision-support system, or automated decision-making system.

Outputs are for technical demonstration only and should not be used for real-world decisions without qualified human review, validation, and appropriate governance controls.

The backend model remains based on medical image risk classification, so the system must not be used for diagnosis, treatment, or clinical decision-making.
