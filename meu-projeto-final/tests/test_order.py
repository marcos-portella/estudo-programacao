import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db_connection

client = TestClient(app)


def test_create_order_success(auth_headers):
    payload = {"name": "Test User ID", "age": 40}

    response = client.post("/customers/", json=payload, headers=auth_headers)
    assert response.status_code == 200

    data = response.json()
    new_id = data.get("id")

    assert new_id is not None
    assert data["message"] == "Customer created successfully"
    assert data["data"]["name"] == payload["name"]

    try:
        payload = {
            "description": "Pedido de Teste Marcos",
            "amount": 150.50,
            "customer_id": new_id
        }

        response = client.post("/orders/", json=payload, headers=auth_headers)
        assert response.status_code == 200
        assert "Pedido criado com sucesso" in response.json()["message"]

    finally:
        conn = get_db_connection()
        if conn is not None:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM customers WHERE id = %s", (new_id,)
                    )
                conn.commit()
            finally:
                conn.close()
        else:
            pytest.fail(
                "Não foi possível conectar ao banco para limpar o rastro "
                "do teste.")


def test_orders_dashboard_stats(auth_headers):
    response = client.get("/orders/stats", headers=auth_headers)
    assert response.status_code == 200

    data = response.json()
    # Verificamos se as chaves que o SQL retorna existem
    assert "total_revenue" in data
    assert "total_orders" in data
    assert isinstance(data["total_revenue"], float)


def test_create_order_invalid_customer(auth_headers):
    payload = {
        "description": "Pedido Fantasma",
        "amount": 100.0,
        "customer_id": 999999  # ID que não existe
    }
    response = client.post("/orders/", json=payload, headers=auth_headers)
    assert response.status_code == 404
    assert "Cliente não encontrado" in response.json()["detail"]


def test_create_order_negative_amount(auth_headers):
    payload = {"name": "Test User ID", "age": 40}

    response = client.post("/customers/", json=payload, headers=auth_headers)
    assert response.status_code == 200

    data = response.json()
    new_id = data.get("id")

    assert new_id is not None
    assert data["message"] == "Customer created successfully"
    assert data["data"]["name"] == payload["name"]

    try:
        payload = {
            "description": "Pedido Grátis",
            "amount": -50.0,
            "customer_id": new_id
        }
        response = client.post("/orders/", json=payload, headers=auth_headers)
        assert response.status_code == 422  # Erro de validação

    finally:
        conn = get_db_connection()
        if conn is not None:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM customers WHERE id = %s", (new_id,)
                    )
                conn.commit()
            finally:
                conn.close()
        else:
            pytest.fail(
                "Não foi possível conectar ao banco para limpar o rastro "
                "do teste.")


def test_get_stats_without_auth():
    # Aqui NÃO passamos o auth_headers
    response = client.get("/orders/stats")
    assert response.status_code == 401
