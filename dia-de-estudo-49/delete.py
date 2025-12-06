import sqlite3

from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Create Read   Update Delete
# SQL -  INSERT SELECT UPDATE DELETE

# CUIDADO: fazendo delete sem where
# cursor.execute(
#     f'DELETE FROM {TABLE_NAME}'
# )

# DELETE mais cuidadoso
# cursor.execute(
#     f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
# )

# connection.commit()

cursor.execute(
    f'DELETE FROM {TABLE_NAME} '
    'WHERE id = "6"'
)
cursor.execute(
    f'DELETE FROM {TABLE_NAME} '
    'WHERE id = 1'
)
connection.commit()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

cursor.close()
connection.close()
