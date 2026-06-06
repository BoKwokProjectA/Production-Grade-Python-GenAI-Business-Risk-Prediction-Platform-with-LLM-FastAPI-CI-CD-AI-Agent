def test_app_imports():
    from src.api.main import app

    routes = {route.path for route in app.routes}

    assert "/" in routes
    assert "/api/v1/health" in routes
    assert "/api/v1/predict" in routes
