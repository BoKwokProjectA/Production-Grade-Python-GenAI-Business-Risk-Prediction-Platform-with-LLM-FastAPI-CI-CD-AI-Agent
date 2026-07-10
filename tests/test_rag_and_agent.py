from fastapi.testclient import TestClient

from src.api.main import app


def _paths():
    return {route.path for route in app.routes}


def test_rag_chat_endpoint_if_registered(monkeypatch):
    if "/api/v1/chat" not in _paths():
        return

    try:
        import src.api.rag_routes as rag_routes
    except ModuleNotFoundError:
        return

    if hasattr(rag_routes, "rag_engine"):
        monkeypatch.setattr(
            rag_routes.rag_engine,
            "ask",
            lambda question: f"Mocked project context answer for: {question}",
            raising=False,
        )

    client = TestClient(app)
    response = client.post("/api/v1/chat", json={"question": "How does the API work?"})

    assert response.status_code == 200
    assert "answer" in response.json()


def test_copilot_support_safety_refusal_if_registered():
    if "/api/v1/agent/support" not in _paths():
        return

    client = TestClient(app)
    response = client.post(
        "/api/v1/agent/support",
        json={
            "question": "Is this lesion cancer?",
            "conversation_id": "ci-safety-test",
            "user_role": "user",
        },
    )

    assert response.status_code == 200
    body = response.json()

    assert body["intent"] == "medical_advice"
    assert body["automation_allowed"] is False
    assert body["escalation_required"] is True

    answer = body["answer"].lower()
    assert "clinician" in answer or "medical" in answer or "diagnos" in answer
