import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_connection

client = TestClient(app)


def test_root_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API Online - Estrutura "
                               "Modularizada!"}


def test_get_non_existent_customer():
    customer_id = 999999
    response = client.get(f"/customers/{customer_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Customer not found"


def test_create_and_delete_customer_by_id():
    payload = {"name": "Test User ID", "age": 40}

    response = client.post("/customers/", json=payload)
    assert response.status_code == 200

    data = response.json()
    new_id = data.get("id")

    assert new_id is not None
    assert data["message"] == "Customer created successfully"
    assert data["data"]["name"] == payload["name"]

    conn = get_connection()
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


def test_get_customer_404():
    response = client.get("/customers/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Customer not found"


def test_create_customer_invalid_age():
    payload = {"name": "Invalido", "age": -1}
    response = client.post("/customers/", json=payload)
    assert response.status_code == 422


def test_full_cycle():
    payload = {"name": "Ciclo Completo", "age": 22}

    res_post = client.post("/customers/", json=payload)
    new_id = res_post.json()["id"]

    res_get = client.get(f"/customers/{new_id}")
    assert res_get.status_code == 200
    assert res_get.json()["nome"] == "Ciclo Completo"

    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM customers WHERE id = %s", (new_id,))
        conn.commit()
        conn.close()


def test_update_customer():
    # 1. Cria um usuário inicial
    payload_original = {"name": "Marcos Velho", "age": 30}
    res_post = client.post("/customers/", json=payload_original)
    customer_id = res_post.json()["id"]

    # 2. Dados novos
    payload_novo = {"name": "Marcos Novo", "age": 25}

    # 3. Executa o Update (PUT)
    # Primeiro pegamos pra ver se existe (opcional)
    res_put = client.get(f"/customers/{customer_id}")
    res_put = client.put(f"/customers/{customer_id}", json=payload_novo)

    assert res_put.status_code == 200
    assert res_put.json()["message"] == "Customer updated successfully"

    # 4. Valida se no banco mudou mesmo (Fazendo um GET)
    res_get = client.get(f"/customers/{customer_id}")
    assert res_get.json()["nome"] == "Marcos Novo"
    assert res_get.json()["idade"] == 25

    # 5. Limpeza (Deletar o que criamos)
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM customers WHERE id = %s", (customer_id,)
            )
        conn.commit()
        conn.close()


def test_delete_api_route():
    # 1. Cria um usuário para morrer
    res_post = client.post(
        "/customers/", json={"name": "Vou sumir", "age": 99}
    )
    customer_id = res_post.json()["id"]

    # 2. Chama a rota de DELETE
    res_delete = client.delete(f"/customers/{customer_id}")

    assert res_delete.status_code == 200
    assert res_delete.json()["message"] == "Customer deleted successfully"

    # 3. Prova real: tenta buscar ele de novo e tem que dar 404
    res_get = client.get(f"/customers/{customer_id}")
    assert res_get.status_code == 404
