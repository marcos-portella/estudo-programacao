import os
import pytest
from fastapi.testclient import TestClient
from app.main import app
from dotenv import load_dotenv

load_dotenv()

client = TestClient(app)


@pytest.fixture(scope="session")
def auth_headers():

    email = os.getenv("TEST_USER_EMAIL", "")
    password = os.getenv("TEST_USER_PASSWORD", "")

    login_data = {"username": email, "password": password}
    response = client.post("/auth/login", data=login_data)

    if response.status_code != 200:
        pytest.fail(f"Falha no login global: {response.text}")

    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
