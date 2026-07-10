"""Test configuration that prevents real external calls in CI."""

import os

os.environ.setdefault("APP_NAME", "AI-Risk-Platform")
os.environ.setdefault("API_VERSION", "v1")
os.environ.setdefault("MODEL_VERSION", "2024-ensemble-2models")
os.environ.setdefault("DEBUG", "False")
os.environ.setdefault("DATABASE_URL", "sqlite:///./test_isic.db")
os.environ.setdefault("SECRET_KEY", "ci-test-secret-key")
os.environ.setdefault("POWER_AUTOMATE_URL", "")
os.environ.setdefault("OPENAI_API_KEY", "sk-ci-dummy-not-used")
os.environ.setdefault("CI", "true")
