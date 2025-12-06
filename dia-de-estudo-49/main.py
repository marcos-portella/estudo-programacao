import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: fazendo delete sem where

# # A instrução DELETE ABAIXO APAGA TUDO
# cursor.execute(
#     f'DELETE FROM {TABLE_NAME}'
# )
# # A instrução DELETE ABAIXO RESETA o contador AUTOINCREMENT
# cursor.execute(
#     f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
# )
# connection.commit()

# Cria a tabela (mantida para garantir que a estrutura exista):
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weigth REAL'
    ')'
)
connection.commit()

# # Registrando valores na tabela: (COMENTADO!)
# cursor.execute(
#     f'INSERT INTO {TABLE_NAME} (name, weigth) '
#     'VALUES ("Luís Otávio", 9.9)'
# )
# connection.commit()

# # Forma mais segura de escrever o código: (COMENTADO!)
# sql = (
#     f'INSERT INTO {TABLE_NAME} '
#     '(name, weigth) '
#     'VALUES '
#     '(?, ?)'
# )
# cursor.execute(sql, ['joana', 4])
# connection.commit()

# # Este insere vários valores nas colunas da tabela: (COMENTADO!)
# sql = (
#     f'INSERT INTO {TABLE_NAME} '
#     '(name, weigth) '
#     'VALUES '
#     '(?, ?)'
# )
# cursor.executemany(
#     sql,
#     (
#         ('Kakaka', 6), ('Mamani', 7), ('Padre', 3)
#     )
# )
# connection.commit()

# # Usando dicionários: (COMENTADO!)
# sql = (
#     f'INSERT INTO {TABLE_NAME} '
#     '(name, weigth) '
#     'VALUES '
#     '(:nome, :weigth)'
# )
# cursor.executemany(
#     sql,
#     (
#         {'nome': 'yousoo', 'weigth': 50},
#         {'nome': 'Kuma', 'weigth': 90}
#     )
# )
# connection.commit()

# cursor.execute(f'SELECT * FROM {TABLE_NAME}')
# for row in cursor.fetchall():
#     _id, name, weigth = row
#     print(_id, name, weigth)

cursor.close()
connection.close()
