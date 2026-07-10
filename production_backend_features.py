#!/usr/bin/env python
# coding: utf-8

# In[1]:


from google.colab import drive
drive.mount('/content/drive', force_remount=True)


# In[2]:


get_ipython().system('pip install structlog -q')


# In[3]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/db/models.py', '"""\nDatabase models for storing prediction records\n"""\n\nfrom sqlalchemy import Column, Integer, String, Float, DateTime, Text\nfrom sqlalchemy.ext.declarative import declarative_base\nfrom datetime import datetime\n\nBase = declarative_base()\n\nclass PredictionRecord(Base):\n    __tablename__ = "predictions"\n\n    id = Column(Integer, primary_key=True, index=True)\n    isic_id = Column(String, index=True)\n    probability = Column(Float)\n    prediction = Column(String)\n    model_version = Column(String)\n    timestamp = Column(DateTime, default=datetime.utcnow)\n    image_filename = Column(String, nullable=True)\n    user_feedback = Column(String, nullable=True)\n\n')


# In[4]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/repositories/prediction_repo.py', '"""\nRepository layer for prediction records\n"""\n\nfrom sqlalchemy.orm import Session\nfrom src.db.models import PredictionRecord\nfrom datetime import datetime\n\nclass PredictionRepository:\n    def __init__(self, db: Session):\n        self.db = db\n\n    def save_prediction(self, isic_id: str, probability: float, prediction: str,\n                       model_version: str, image_filename: str = None):\n        record = PredictionRecord(\n            isic_id=isic_id,\n            probability=probability,\n            prediction=prediction,\n            model_version=model_version,\n            timestamp=datetime.utcnow(),\n            image_filename=image_filename\n        )\n        self.db.add(record)\n        self.db.commit()\n        self.db.refresh(record)\n        return record\n\n')


# In[5]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/core/logger.py', '"""\nStructured logging configuration\n"""\n\nimport structlog\n\n\nstructlog.configure(\n    processors=[\n        structlog.processors.JSONRenderer()\n    ],\n    logger_factory=structlog.PrintLoggerFactory(),\n)\n\nlogger = structlog.get_logger()\n\n')


# In[6]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/api/main.py', '"""\nMain FastAPI application\n"""\n\nfrom fastapi import FastAPI\nfrom fastapi.middleware.cors import CORSMiddleware\nfrom contextlib import asynccontextmanager\n\nfrom src.core.config import get_settings\nfrom src.core.logger import logger\nfrom src.api.routes import health_router, prediction_router\nfrom src.api.rag_routes import rag_router\n\nsettings = get_settings()\n\n@asynccontextmanager\nasync def lifespan(app: FastAPI):\n    logger.info("Application starting up", app_name=settings.APP_NAME)\n    yield\n    logger.info("Application shutting down")\n\napp = FastAPI(\n    title=settings.APP_NAME,\n    version=settings.API_VERSION,\n    description="ISIC 2024 Skin Cancer Detection API",\n    lifespan=lifespan\n)\n\napp.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])\n\napp.include_router(health_router, prefix="/api/v1", tags=["health"])\napp.include_router(prediction_router, prefix="/api/v1", tags=["prediction"])\napp.include_router(rag_router, prefix="/api/v1", tags=["rag"])\n\n@app.get("/")\nasync def root():\n    logger.info("Root endpoint accessed")\n    return {"message": "ISIC 2024 Flagship API is running"}\n\n')

