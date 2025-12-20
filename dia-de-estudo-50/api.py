import os
import pymysql
import dotenv
from fastapi import FastAPI  # 1. Importa o FastAPI

dotenv.load_dotenv()
app = FastAPI()  # 2. Cria a instância do aplicativo

TABLE_NAME = 'custumers'


# Função para conectar ao banco (igual ao que você já faz)
def get_connection():
    return pymysql.connect(
        host=os.environ['MYSQL_HOST'],
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        database=os.environ['MYSQL_DATABASE'],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor  # 3. IMPORTANTE: Retorna como
                                                # dicionário para a API
                                                # entender
    )


# 4. Criando a "Rota" (o endereço que você vai acessar)
@app.get("/clientes")
def listar_clientes():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Seleciona tudo da sua tabela
            cursor.execute(f"SELECT * FROM {TABLE_NAME}")
            dados = cursor.fetchall()
            return dados  # 5. O FastAPI transforma isso em JSON
            # automaticamente!
    finally:
        connection.close()


# Rota para cadastrar um novo usuário
@app.post("/cadastrar")
def cadastrar_cliente(nome: str, idade: int):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = f"INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%s, %s)"
            cursor.execute(sql, (nome, idade))
        connection.commit()
        return {"mensagem": f"Usuário {nome} cadastrado com sucesso!"}
    except Exception as e:
        return {"erro": str(e)}
    finally:
        connection.close()
