from app.database import get_connection
from fastapi import HTTPException
from typing import Generator


def get_db() -> Generator:
    connection = get_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection "
                            "failed")
    try:
        # O 'yield' faz a mágica: ele entrega a conexão para a rota
        # e FICA ESPERANDO a rota terminar para continuar a execução.
        yield connection
    finally:
        # Assim que a rota envia a resposta para o usuário,
        # o código volta para cá e fecha a conexão AUTOMATICAMENTE.
        connection.close()
        print("Conexão fechada automaticamente pelo Depends")
