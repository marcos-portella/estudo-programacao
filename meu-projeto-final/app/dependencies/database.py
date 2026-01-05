from typing import Generator
from fastapi import HTTPException
from app.database import get_db_connection


def get_db() -> Generator:
    connection = get_db_connection()
    if connection is None:
        raise HTTPException(
            status_code=500, detail="Database connection failed"
        )
    try:
        yield connection
    finally:
        connection.close()
        print("Conexão fechada automaticamente pelo Depends")
