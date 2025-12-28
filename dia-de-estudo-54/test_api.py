import pytest
from fastapi.testclient import TestClient
from main import app  # Ele vai procurar o 'main' que está na mesma pasta

client = TestClient(app)


def test_root_status():
    """Verifica se a API está online"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API Online - Estrutura "
                               "Modularizada!"}


def test_get_non_existent_customer():
    """Verifica se a API retorna 404 para um cliente que não existe"""
    # Usamos um ID que provavelmente não existe (ex: 999999)
    customer_id = 999999
    response = client.get(f"/customers/{customer_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Customer not found"


def test_create_and_delete_test_user():
    """Cria um usuário e o apaga logo em seguida para não sujar o banco"""
    nome_teste = "User Temporario Teste"
    payload = {"name": nome_teste, "age": 25}

    # 1. Criar o usuário
    response_post = client.post("/customers/", json=payload)
    assert response_post.status_code == 200

    # 2. Apagar o usuário criado (Usando uma rota de delete se você tiver,
    # ou podemos fazer um pequeno 'truque' via código de banco no próprio
    # teste)
    from database import get_connection
    conn = get_connection()

    if conn is None:
        pytest.fail("Database connection failed during cleanup")

    try:
        with conn.cursor() as cursor:
            # Apaga especificamente o nome que acabamos de usar no teste
            sql = "DELETE FROM customers WHERE nome = %s"
            cursor.execute(sql, (nome_teste,))
        conn.commit()
    finally:
        conn.close()

    print(f"\n✅ Usuário '{nome_teste}' criado e removido automaticamente!")


def test_create_customer_invalid_age():
    """Verifica se a API bloqueia idades absurdas (ex: -1)"""
    payload = {"name": "Invalido", "age": -1}
    response = client.post("/customers/", json=payload)

    # O FastAPI retorna 422 automaticamente quando a validação do Pydantic
    # falha
    assert response.status_code == 422
