import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: fazendo delete sem where

cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Cria a tabela:
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id  INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weigth REAL'
    ')'
)
connection.commit()

# Registrando valores na tabela:
# CUIDADO: sql injection
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (name, weigth) '
    'VALUES ("Luís Otávio", 9.9)'
)
connection.commit()

# Forma mais segura de escrever o código:
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weigth) '
    'VALUES '
    '(?, ?)'
)
cursor.execute(sql, ['joana', 4])
connection.commit()

cursor.close()
connection.close()
