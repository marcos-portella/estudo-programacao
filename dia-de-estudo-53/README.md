### Dia 53: Refatoração para Arquitetura Modular e Segurança

### Prefácio:

No **Dia 53**, o foco saiu da funcionalidade bruta para a excelência na **organização de código** e **segurança de infraestrutura**. O objetivo principal foi a transição de um script único para uma **Arquitetura Modular**, utilizando o ``APIRouter`` do FastAPI. Além de organizar o projeto como sistemas de mercado, implementamos camadas de segurança com variáveis de ambiente e reforçamos o tratamento de erros de conexão, preparando a API para ambientes de produção.

### 1. Camada de Conexão Independente (database.py):

Centralizamos a lógica de acesso ao banco de dados em um arquivo dedicado. Isso evita a repetição de código e facilita a manutenção. Introduzimos o uso do ``python-dotenv`` para carregar credenciais sensíveis (como senhas) a partir de um arquivo ``.env``, garantindo que informações críticas não fiquem expostas no código-fonte.

````
import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv() # Carrega as variáveis do arquivo .env

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
        print(f"Erro de conexão MySQL: {e}")
        return None # Retorna None para ser tratado pela cláusula de guarda
````

### 2. Modularização com APIRouter (routers/customers.py):

Utilizamos o ``APIRouter`` para isolar a lógica de clientes. Com o uso de ``prefix`` e ``tags``, o código fica mais limpo e a documentação (Swagger) mais organizada. Aqui, aplicamos a **Cláusula de Guarda**: se a conexão com o banco falhar, a API interrompe o processo imediatamente com um erro 500, protegendo a execução.

````
from fastapi import APIRouter, HTTPException
from database import get_connection
from pydantic import BaseModel

router = APIRouter(prefix="/customers", tags=["Customers"])

class Customer(BaseModel):
    name: str
    age: int

@router.post("/")
def create_customer(customer: Customer):
    connection = get_connection()
    if connection is None: # Cláusula de Guarda: Tratamento de falha de infraestrutura
        raise HTTPException(status_code=500, detail="Database connection failed")
    try:
        with connection.cursor() as cursor:
            # Resolvido erro 1054: Mapeando coluna do banco (nome) vs atributo (name)
            sql = "INSERT INTO customers (nome, idade) VALUES (%s, %s)"
            cursor.execute(sql, (customer.name, customer.age))
        connection.commit()
        return {"message": "Customer created successfully"}
    finally:
        connection.close()
````

### 3. Orquestrador Principal (main.py):

Com a lógica movida para os routers, o arquivo ``main.py`` torna-se um orquestrador leve. Sua única função agora é instanciar o FastAPI e incluir as rotas modulares. Esta estrutura permite que o projeto cresça indefinidamente (ex: adicionando ``products.py``, ``orders.py``) sem poluir o arquivo principal.

````
from fastapi import FastAPI
from routers import customers

app = FastAPI()

# Incluindo o módulo de clientes na aplicação principal
app.include_router(customers.router)

@app.get("/")
def root():
    return {"message": "API Online - Estrutura Modularizada!"}
````

### 4. Resolução de Erros de SQL (Debug de Produção):

Um dos grandes aprendizados de hoje foi o tratamento do **Erro 1054 (Unknown column)**. Entendemos que existe uma diferença vital entre os nomes das colunas no MySQL (ex: ``nome``) e os nomes das variáveis no Python/Pydantic (ex: ``name``). O código abaixo ilustra como mapear essas diferenças corretamente na consulta SQL.

````
# Correção de nomenclatura entre Código e Banco
# SQL usa o nome da coluna física | Tuple usa o atributo do Pydantic
sql = "UPDATE customers SET nome = %s, idade = %s WHERE id = %s"
valores = (customer.name, customer.age, customer_id)
# cursor.execute(sql, valores)
````

### Observações Finais:

O **Dia 53** consolidou a importância da arquitetura sobre a sintaxe. Aprendemos que separar responsabilidades (Database vs Routers vs Main) torna o sistema testável e seguro. A implementação das variáveis de ambiente é um marco de maturidade técnica, e a resolução de conflitos de nomes entre Banco de Dados e API reforçou a necessidade de atenção ao mapeamento de dados (ORM feeling).