from app.core.config import settings
from fastapi.testclient import TestClient


def test_login(client: TestClient) -> None:
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PW,
    }
    r = client.post(f"{settings.API_V1_STR}/login", data=login_data)
    response = r.json()
    assert r.status_code == 200
    assert "access_token" in response
    assert response["access_token"]

