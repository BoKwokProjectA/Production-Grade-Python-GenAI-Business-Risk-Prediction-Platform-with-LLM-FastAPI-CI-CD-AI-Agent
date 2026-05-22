"""
Main FastAPI application.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.config import get_settings
from src.api.routes import health_router, prediction_router
from src.api.copilot_routes import copilot_router


settings = get_settings()

app = FastAPI(
    title="ISIC Skin Lesion Platform API",
    version=settings.API_VERSION,
    description="ISIC Skin Lesion Detection API with Copilot Studio support endpoints",
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
        "openapi_url": "/openapi.json",
    }


app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["health"],
)

app.include_router(
    prediction_router,
    prefix="/api/v1",
    tags=["prediction"],
)

app.include_router(
    copilot_router,
    prefix="/api/v1",
    tags=["copilot-studio"],
)
