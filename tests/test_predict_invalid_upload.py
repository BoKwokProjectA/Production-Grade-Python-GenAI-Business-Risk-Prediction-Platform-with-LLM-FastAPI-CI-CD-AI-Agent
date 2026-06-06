from fastapi.testclient import TestClient

from src.api.main import app


def test_predict_rejects_non_image_upload():
    client = TestClient(app)

    response = client.post(
        "/api/v1/predict",
        files={"file": ("not-an-image.txt", b"not image bytes", "text/plain")},
    )

    assert response.status_code == 400
    assert "image" in response.json()["detail"].lower()
