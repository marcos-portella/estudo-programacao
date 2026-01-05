import mysql.connector
from mysql.connector import Error
import os


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE"),
            # Dica: adicione um timeout para a API não ficar travada esperando
            connect_timeout=5
        )
        if connection.is_connected():
            return connection

    except Error as e:
        print(f"❌ Erro ao conectar ao MySQL: {e}")
# Aqui podes decidir: ou para o sistema, ou levanta uma exceção para o FastAPI
        return None


# No FastAPI, usamos o gerador (yield) para garantir que fecha a conexão
def get_db():
    db = get_db_connection()
    if db is None:
        # Se o banco estiver fora, avisamos o usuário da API de forma elegante
        from fastapi import HTTPException
        raise HTTPException(
            status_code=503,
            detail="Banco de dados temporariamente indisponível"
        )
    try:
        yield db
    finally:
        if db.is_connected():
            db.close()
