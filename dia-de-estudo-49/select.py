import sqlite3

from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME} LIMIT 0,2')

for row in cursor.fetchall():
    _id, name, weigth = row
    print(_id, name, weigth)

print()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"'
    )

row = cursor.fetchone()
print(row)

cursor.close()
connection.close()
