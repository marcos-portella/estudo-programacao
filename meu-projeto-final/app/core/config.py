import os
from dotenv import load_dotenv

# Carrega as variáveis do ficheiro .env para o sistema
load_dotenv()


class Settings:
    PROJECT_NAME: str = "Meu Projeto Final"

    # Busca do .env ou usa um valor padrão (default)
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_DATABASE = os.getenv("DB_DATABASE")

    API_KEY = os.getenv("API_KEY")


settings = Settings()
