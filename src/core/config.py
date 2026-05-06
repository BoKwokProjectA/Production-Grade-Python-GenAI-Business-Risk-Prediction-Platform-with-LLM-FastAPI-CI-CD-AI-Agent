"""
Core configuration
"""

from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "ISIC 2024 Skin Cancer Detection"
    API_VERSION: str = "v1"
    MODEL_VERSION: str = "2024-ensemble-v1"
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite+aiosqlite:///./isic.db"
    NGROK_AUTHTOKEN: str = ""
    SECRET_KEY: str = "super-secret-key-change-in-production"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


