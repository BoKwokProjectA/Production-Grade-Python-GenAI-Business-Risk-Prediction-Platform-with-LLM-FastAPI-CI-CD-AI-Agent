"""
Main FastAPI application.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.copilot_routes import copilot_router
from src.api.routes import health_router, prediction_router
from src.core.config import get_settings

settings = get_settings()

tags_metadata = [
    {
        "name": "prediction",
        "description": "Upload an image and receive a structured risk scoring response.",
    },
    {
        "name": "health",
        "description": "Health check endpoints.",
    },
    {
        "name": "copilot-studio",
        "description": "Support endpoints used by the Copilot Studio custom connector.",
    },
    {
        "name": "general",
        "description": "General API information.",
    },
]

app = FastAPI(
    title="AI Risk Prediction Platform API",
    version=settings.API_VERSION,
    description=(
        "AI risk scoring API with image upload, prediction, health check, and support-agent endpoints."
    ),
    openapi_tags=tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["general"])
async def root():
    return {
        "status": "ok",
        "service": "AI Risk Prediction Platform API",
        "docs_url": "/docs",
        "openapi_url": "/openapi.json",
    }


app.include_router(
    prediction_router,
    prefix="/api/v1",
    tags=["prediction"],
)

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["health"],
)

app.include_router(
    copilot_router,
    prefix="/api/v1",
    tags=["copilot-studio"],
)
