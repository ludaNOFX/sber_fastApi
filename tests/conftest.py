from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient

from app.db.session import SessionLocal
from app.main import app
from .utils.utils import get_employee_user_token, get_regular_user_token


@pytest.fixture(scope='session')
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope='session')
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope='session')
def employee_user_headers(client: TestClient) -> Dict[str, str]:
    return get_employee_user_token(client)


@pytest.fixture(scope='session')
def regular_user_headers(client: TestClient) -> Dict[str, str]:
    return get_regular_user_token(client)
