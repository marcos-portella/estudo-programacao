## Dia 49: Introdução ao SQL com Python (SQLite)

### Prefácio:

No Dia 49, iniciamos a exploração da integração entre a linguagem de programação **Python** e bancos de dados relacionais, utilizando o módulo ``sqlite3`` para gerenciar um banco de dados **SQLite**. O foco foi estabelecer uma conexão com o banco, criar tabelas, e realizar operações básicas de Inserção (CREATE), Leitura (READ), Atualização (UPDATE) e Exclusão (DELETE) de dados, o que é fundamental para qualquer aplicação que precise persistir informações.

### Estabelecendo a Conexão com o Banco de Dados:

O primeiro passo é importar o módulo ``sqlite3`` e criar uma conexão com o arquivo do banco de dados (neste caso, ``base.db``). Se o arquivo não existir, o ``sqlite3`` o criará automaticamente. É essencial criar um cursor a partir da conexão. O cursor é o objeto que permite executar comandos SQL dentro da sessão do Python.

````
# Exemplo 1: Conexão e Criação do Cursor
import sqlite3
from pathlib import Path

# Conectar ao banco de dados (ou criar se não existir)
ROOT_PATH = Path(__file__).parent
db_path = ROOT_PATH / 'base.db'
connection = sqlite3.connect(db_path) 

# Criar o cursor
cursor = connection.cursor()
````

### Criando Tabelas e Executando Comandos SQL:

A execução de comandos SQL é feita pelo método ``cursor.execute()``. Para criar uma tabela (``CREATE TABLE``), definimos o nome da tabela e os campos com seus respectivos tipos de dados (e.g., ``id INTEGER PRIMARY KEY``, ``nome TEXT``, ``peso REAL``).

O comando ``DROP TABLE IF EXISTS`` é frequentemente usado antes do ``CREATE TABLE`` em ambientes de desenvolvimento para garantir que a tabela seja recriada do zero, evitando erros de duplicidade.

````
# Exemplo 2: Comando SQL para Criação de Tabela
# Deleta a tabela se ela existir
cursor.execute(
    'DROP TABLE IF EXISTS clientes;'
)

# Cria a tabela clientes
cursor.execute(
    'CREATE TABLE IF NOT EXISTS clientes ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome TEXT,'
    'peso REAL'
    ');'
)
````

### Inserção de Dados (CREATE):

A inserção de dados pode ser feita de duas maneiras principais:

- **Inserção Simples**: Usando ``cursor.execute()`` com valores literais na string SQL.

- **Inserção Segura/Múltipla**: Usando ``cursor.executemany()`` ou ``cursor.execute()`` com **placeholders** (``?``) e uma tupla de dados, o que previne ataques de injeção de SQL e é a forma **recomendada**.

````
# Exemplo 3: Inserção Múltipla e Segura (CRUD - Create)
dados_clientes = [
    ('Julia', 60),
    ('Luiz', 70),
    ('Maria', 75.5),
]

cursor.executemany(
    'INSERT INTO clientes (nome, peso) VALUES (?, ?)',
    dados_clientes
)
````

### Compromisso da Transação e Encerramento:

Após executar comandos que modificam o banco de dados (como ``INSERT``, ``UPDATE`` ou ``DELETE``), é crucial chamar o método ``connection.commit()`` para **salvar permanentemente** as alterações no arquivo ``base.db``. Se isso não for feito, as alterações só existirão na memória durante a execução do script. Por fim, a conexão deve ser encerrada com ``connection.close()``.

````
# Exemplo 4: Commit e Fechamento da Conexão
# Salvar as alterações no banco de dados
connection.commit()

# Fechar a conexão
connection.close()
````

### Observações Finais:

A integração do Python com SQL via ``sqlite3`` é um modelo de como a maioria das interações com bancos de dados funciona. O padrão de abrir a conexão, obter um **cursor**, **executar** comandos SQL, fazer o **commit** e **fechar** a conexão é fundamental. O uso de placeholders (``?``) com tuplas para inserção de dados não é apenas uma boa prática, mas uma medida de segurança essencial contra a injeção de SQL.
