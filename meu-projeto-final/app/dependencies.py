import os
from dotenv import load_dotenv
from app.database import get_connection
from fastapi import Security, HTTPException, status
from typing import Generator
from fastapi.security.api_key import APIKeyHeader

load_dotenv()


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


# Busca a chave do ambiente. Se não existir, o padrão é None
API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "X-API-KEY"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(api_key_header: str = Security(api_key_header)):
    # Validação robusta: se a chave não estiver no .env ou for errada, bloqueia
    if api_key_header == API_KEY and API_KEY is not None:
        return api_key_header

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Acesso negado: API Key inválida ou ambiente não configurado"
    )
