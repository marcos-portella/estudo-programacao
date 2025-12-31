import pytest
from fastapi.testclient import TestClient
from main import app
from database import get_connection

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
    """
    Fluxo completo: Cria o usuário, captura o ID gerado pelo banco,
    valida a resposta e deleta usando o ID exato.
    """
    # 1. Dados para o teste
    payload = {"name": "Test User ID", "age": 40}

    # 2. Executa o POST
    response = client.post("/customers/", json=payload)
    assert response.status_code == 200

    # 3. Captura o ID retornado pela sua nova lógica de lastrowid
    data = response.json()
    new_id = data.get("id")

    # Validações básicas
    assert new_id is not None
    assert data["message"] == "Customer created successfully"
    assert data["data"]["name"] == payload["name"]

    # 4. Limpeza (Teardown) usando o ID
    conn = get_connection()
    if conn is not None:
        try:
            with conn.cursor() as cursor:
                # Agora usamos o ID, o que é muito mais seguro!
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
    """Verifica se a API retorna 404 para ID inexistente"""
    response = client.get("/customers/999999")
    assert response.status_code == 404
    # Lembre-se de conferir se no seu código está "Customer" ou "Customers"
    assert response.json()["detail"] == "Customer not found"


def test_create_customer_invalid_age():
    payload = {"name": "Invalido", "age": -1}
    response = client.post("/customers/", json=payload)
    assert response.status_code == 422


def test_full_cycle():
    """Teste de Ciclo Completo: Cria -> Busca por ID -> Deleta"""
    payload = {"name": "Ciclo Completo", "age": 22}

    # 1. Cria
    res_post = client.post("/customers/", json=payload)
    new_id = res_post.json()["id"]

    # 2. Busca o que acabou de criar
    res_get = client.get(f"/customers/{new_id}")
    assert res_get.status_code == 200
    assert res_get.json()["nome"] == "Ciclo Completo"

    # 3. Limpa (Deleta)
    conn = get_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM customers WHERE id = %s", (new_id,))
        conn.commit()
        conn.close()
