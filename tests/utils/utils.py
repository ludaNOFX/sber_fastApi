from typing import Dict

from fastapi.testclient import TestClient

from app.core.config import settings

import random
import string


def get_employee_user_token(client: TestClient) -> Dict[str, str]:
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PW,
    }
    r = client.post(f"{settings.API_V1_STR}/login", data=login_data)
    response = r.json()
    acc_token = response['access_token']
    headers = {"Authorization": f"Bearer {acc_token}"}
    return headers


def get_regular_user_token(client: TestClient) -> Dict[str, str]:
    login_data = {
        "username": settings.TEST_USER_EMAIL,
        "password": settings.TEST_USER_PW,
    }
    r = client.post(f"{settings.API_V1_STR}/login", data=login_data)
    response = r.json()
    acc_token = response['access_token']
    headers = {"Authorization": f"Bearer {acc_token}"}
    return headers


def random_string() -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=10))


def random_email() -> str:
    return f"{random_string()}@{random_string()}.com"


def random_password() -> str:
    return random_string()