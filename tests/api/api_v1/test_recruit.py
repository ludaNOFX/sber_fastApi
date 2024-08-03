from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_stacks(client: TestClient, employee_user_headers: dict) -> None:
    r = client.get(f"{settings.API_V1_STR}/recruit/stacks", headers=employee_user_headers)
    assert r.status_code == 200
    response = r.json()
    assert 'results' in response


def test_get_users_classes(client: TestClient, employee_user_headers: dict) -> None:
    data = {"names": "string", "id": 1}
    r = client.post(f"{settings.API_V1_STR}/recruit/classes", json=data, headers=employee_user_headers)
    assert r.status_code == 200
    response = r.json()
    assert 'high' in response
    assert 'mid' in response
    assert 'low' in response
