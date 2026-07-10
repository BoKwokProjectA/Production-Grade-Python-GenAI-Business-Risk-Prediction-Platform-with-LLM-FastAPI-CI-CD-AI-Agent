from fastapi.testclient import TestClient

from src.api.main import app


def test_health_endpoint():
    client = TestClient(app)

    response = client.get("/api/v1/health")

    assert response.status_code == 200
    body = response.json()

    assert body.get("status") in {"healthy", "ok"}
    assert "model_version" in body
