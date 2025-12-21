## Dia 50: Arquitetura de APIs com FastAPI e MySQL

### Prefácio:

O **Dia 50** marca uma transição fundamental: a evolução de scripts isolados para a construção de um sistema conectado e profissional. O foco foi a criação de uma **API (Application Programming Interface)** com o framework **FastAPI**, integrando-a a um banco de dados **MySQL**. Aprendemos a transformar o Python em um servidor capaz de ouvir requisições externas, validar dados automaticamente e persistir informações de forma estruturada e segura.

### 1. Configuração do Ambiente e Conexão Segura:

Para uma aplicação robusta, nunca escrevemos senhas diretamente no código. Utilizamos o ``python-dotenv`` para gerenciar credenciais. A função ``find_dotenv()`` localiza o arquivo ``.env`` na raiz do projeto, permitindo que a conexão funcione corretamente mesmo em subpastas.

````
from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv
import os, pymysql

load_dotenv(find_dotenv()) # Busca o .env na raiz
app = FastAPI()

def get_connection():
    return pymysql.connect(
        host=os.environ['MYSQL_HOST'],
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        database=os.environ['MYSQL_DATABASE'],
        cursorclass=pymysql.cursors.DictCursor # Essencial para retornar JSON
    )
````

### 2. Gestão de Credenciais e Segurança (.env e .gitignore):

O arquivo ``.env`` armazena dados sensíveis, enquanto o ``.gitignor``e garante que esses dados não sejam rastreados pelo Git, protegendo suas senhas de acessos indevidos em repositórios públicos.

````
# Exemplo de arquivo .env (Omitido do Git)
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=minha_senha_segura
MYSQL_DATABASE=db_clientes

# No arquivo .gitignore, adicionamos:
.env
__pycache__/
.venv/
````

### 3. Implementação do Método GET (Leitura):

O método **GET** é utilizado quando queremos solicitar informações do servidor. No contexto de APIs, é fundamental que o retorno seja em formato **JSON**. Ao utilizarmos o ``DictCursor`` na conexão, o FastAPI consegue converter automaticamente o resultado do banco de dados em uma lista de objetos que o navegador ou o front-end conseguem interpretar instantaneamente.

````
@app.get("/clientes")
def listar_clientes():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Busca todos os registros da tabela
            cursor.execute("SELECT * FROM clientes")
            return cursor.fetchall() # O FastAPI converte o DictCursor em JSON automaticamente
    finally:
        conn.close()
````

### 4. Implementação do Método POST (Escrita):

Diferente do GET, o método **POST** é usado para enviar dados ao servidor para serem processados ou armazenados. Uma das grandes vantagens do FastAPI é a validação de tipos: ao definir ``nome: str`` e ``idade: int``, o framework valida os dados antes mesmo de tentar inseri-los no banco de dados, retornando um erro automático caso o formato esteja incorreto.

````
@app.post("/cadastrar")
def cadastrar(nome: str, idade: int): 
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Uso de placeholders (%s) para evitar SQL Injection
            sql = "INSERT INTO clientes (nome, idade) VALUES (%s, %s)"
            cursor.execute(sql, (nome, idade))
        conn.commit() # Salva a alteração no banco
        return {"status": "sucesso", "mensagem": f"Cliente {nome} cadastrado!"}
    finally:
        conn.close()
````

### 5. Execução do Servidor com Uvicorn:

O Uvicorn é o motor que coloca a API no ar. Com o parâmetro ``--reload``, o servidor detecta alterações no código e reinicia sozinho, agilizando o desenvolvimento.

````
# Comando para rodar a aplicação
uvicorn api:app --reload
````

### Observações Finais:

O aprendizado de hoje consolidou a ideia de que o Python pode ser o motor de um sistema completo. O uso do DictCursor foi um ponto chave para que a API devolvesse dados em formato chave-valor prontos para o consumo. Além disso, a documentação automática via ``/docs`` (Swagger) provou ser uma ferramenta poderosa para testar o sistema sem a necessidade de um front-end pronto.