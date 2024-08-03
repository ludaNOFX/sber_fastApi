from fastapi.testclient import TestClient
import pytest

from app.core.config import settings
from tests.utils.utils import random_email, random_password


@pytest.mark.parametrize(
    "data",
    [
        ({"name": "Ciri"}),
        ({"surname": "From Rivia"}),
        ({"city": "Saint-Petersburg"})

    ]
)
def test_update_user(data, *, client: TestClient, regular_user_headers: dict) -> None:
    r = client.put(f"{settings.API_V1_STR}/users/update", json=data, headers=regular_user_headers)
    assert r.status_code == 200
    response = r.json()
    key = [i for i in data.keys()][0]
    assert key in response
    assert response[key] == data[key]


def test_create_user(client: TestClient) -> None:
    data = {"email": random_email(), "password": random_password()}
    r = client.post(f"{settings.API_V1_STR}/users/signup", json=data)
    assert r.status_code == 201


def test_create_exist_user(client: TestClient) -> None:
    data = {"email": settings.TEST_USER_EMAIL, "password": settings.TEST_USER_PW}
    r = client.post(f"{settings.API_V1_STR}/users/signup", json=data)
    assert r.status_code == 400


def test_get_hard_test(client: TestClient, regular_user_headers: dict) -> None:
    r = client.get(f"{settings.API_V1_STR}/users/hard_test", headers=regular_user_headers)
    assert r.status_code == 200
    response = r.json()
    assert response['1']['question']
    assert response['1']['options']
    assert response['1']['correct_answer'] == 0


def test_get_soft_test(client: TestClient, regular_user_headers: dict) -> None:
    r = client.get(f"{settings.API_V1_STR}/users/soft_test", headers=regular_user_headers)
    assert r.status_code == 200
    response = r.json()
    assert response['1']['question']
    assert response['1']['options']
    assert response['1']['correct_answer'] == 0


def test_get_hard_rate(client: TestClient, regular_user_headers: dict) -> None:
    rate_in = {
                "1": {
                    "correct_answer": 0,
                    "user_answer": 1
                },
                "2": {
                    "correct_answer": 0,
                    "user_answer": 0
                },
                "3": {
                    "correct_answer": 0,
                    "user_answer": 0
                },
                "4": {
                    "correct_answer": 0,
                    "user_answer": 1
                },
                "5": {
                    "correct_answer": 0,
                    "user_answer": 0
                },
                "6": {
                    "correct_answer": 0,
                    "user_answer": 0
                },
                "7": {
                    "correct_answer": 0,
                    "user_answer": 1
                },
                "8": {
                    "correct_answer": 0,
                    "user_answer": 0
                },
                "9": {
                    "correct_answer": 0,
                    "user_answer": 0
                },
                "10": {
                    "correct_answer": 0,
                    "user_answer": 1
                }
            }
    r = client.post(f"{settings.API_V1_STR}/users/get_hard_rate", headers=regular_user_headers, json=rate_in)
    assert r.status_code == 200
    response = r.json()
    assert response["hard_rate"]


def test_get_soft_rate(client: TestClient, regular_user_headers: dict) -> None:
    rate_in = {
                "1": {
                    "correct_answer": 0,
                    "user_answer": 0
                },
                "2": {
                    "correct_answer": 0,
                    "user_answer": 0
                },
                "3": {
                    "correct_answer": 0,
                    "user_answer": 0
                },
                "4": {
                    "correct_answer": 0,
                    "user_answer": 0
                },
                "5": {
                    "correct_answer": 0,
                    "user_answer": 0
                },
                "6": {
                    "correct_answer": 0,
                    "user_answer": 0
                },
                "7": {
                    "correct_answer": 0,
                    "user_answer": 1
                },
                "8": {
                    "correct_answer": 0,
                    "user_answer": 0
                },
                "9": {
                    "correct_answer": 0,
                    "user_answer": 0
                },
                "10": {
                    "correct_answer": 0,
                    "user_answer": 0
                }
            }
    r = client.post(f"{settings.API_V1_STR}/users/get_soft_rate", headers=regular_user_headers, json=rate_in)
    assert r.status_code == 200
    response = r.json()
    assert response["soft_rate"]


def test_get_overall_rate(client: TestClient, regular_user_headers: dict) -> None:
    r = client.put(f"{settings.API_V1_STR}/users/get_overall_rate", headers=regular_user_headers)
    assert r.status_code == 200
    response = r.json()
    assert response["rate"]
