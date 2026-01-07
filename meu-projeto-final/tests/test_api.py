import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db_connection

client = TestClient(app)


def test_root_status(auth_headers):
    response = client.get("/", headers=auth_headers)
    assert response.status_code == 200
    assert response.json() == {"message": "API Online - Monitoramento Ativo!"}


def test_get_non_existent_customer(auth_headers):
    customer_id = 999999
    response = client.get(f"/customers/{customer_id}", headers=auth_headers)
    assert response.status_code == 404
    assert response.json()["detail"] == "Customer not found"


def test_create_and_delete_customer_by_id(auth_headers):
    payload = {"name": "Test User ID", "age": 40}

    response = client.post("/customers/", json=payload, headers=auth_headers)
    assert response.status_code == 200

    data = response.json()
    new_id = data.get("id")

    assert new_id is not None
    assert data["message"] == "Customer created successfully"
    assert data["data"]["name"] == payload["name"]

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
        pytest.fail("Não foi possível conectar ao banco para limpar o rastro "
                    "do teste.")


def test_get_customer_404(auth_headers):
    response = client.get("/customers/999999", headers=auth_headers)
    assert response.status_code == 404
    assert response.json()["detail"] == "Customer not found"


def test_create_customer_invalid_age(auth_headers):
    payload = {"name": "Invalido", "age": -1}
    response = client.post("/customers/", json=payload, headers=auth_headers)
    assert response.status_code == 422


def test_full_cycle(auth_headers):
    payload = {"name": "Ciclo Completo", "age": 22}

    res_post = client.post("/customers/", json=payload, headers=auth_headers)
    new_id = res_post.json()["id"]

    res_get = client.get(f"/customers/{new_id}", headers=auth_headers)
    assert res_get.status_code == 200
    assert res_get.json()["nome"] == "Ciclo Completo"

    conn = get_db_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM customers WHERE id = %s", (new_id,))
        conn.commit()
        conn.close()


def test_update_customer(auth_headers):
    # 1. Cria um usuário inicial
    payload_original = {"name": "Marcos Velho", "age": 30}
    res_post = client.post(
        "/customers/", json=payload_original, headers=auth_headers
    )
    customer_id = res_post.json()["id"]

    # 2. Dados novos
    payload_novo = {"name": "Marcos Novo", "age": 25}

    # 3. Executa o Update (PUT)
    # Primeiro pegamos pra ver se existe (opcional)
    res_put = client.get(f"/customers/{customer_id}", headers=auth_headers)
    res_put = client.put(
        f"/customers/{customer_id}", json=payload_novo, headers=auth_headers
    )

    assert res_put.status_code == 200
    assert res_put.json()["message"] == "Customer updated successfully"

    # 4. Valida se no banco mudou mesmo (Fazendo um GET)
    res_get = client.get(f"/customers/{customer_id}", headers=auth_headers)
    assert res_get.json()["nome"] == "Marcos Novo"
    assert res_get.json()["idade"] == 25

    # 5. Limpeza (Deletar o que criamos)
    conn = get_db_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM customers WHERE id = %s", (customer_id,)
            )
        conn.commit()
        conn.close()
