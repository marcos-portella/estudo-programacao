import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv  # Importa a função para carregar o .env

# Carrega as variáveis do arquivo .env para o sistema
load_dotenv()


def get_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE'),
            charset='utf8mb4'
        )
        return connection
    except Error as e:
        print(f"Erro de conexão: {e}")
        return None
