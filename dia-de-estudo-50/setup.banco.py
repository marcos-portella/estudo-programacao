import os

import pymysql
from dotenv import load_dotenv, find_dotenv

TABLE_NAME = 'custumers'

load_dotenv(find_dotenv())

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
)
try:
    with connection:
        with connection.cursor() as cursor:  # Cuidado com sql injection
            cursor.execute(  # type: ignore
                f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
                'id INT NOT NULL AUTO_INCREMENT, '
                'nome VARCHAR(50) NOT NULL, '
                'idade INT NOT NULL, '
                'PRIMARY KEY (id)'
                ') '
            )
        connection.commit()

        with connection.cursor() as cursor:
            sql = f'INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%s, %s)'

            # Uma lista de tuplas com os dados
            dados = [
                ("Gabriela", 34),
                ("Miguel", 12),
                ("Ana", 25)
            ]

            # O executemany faz o loop e insere todos de uma vez
            result = cursor.executemany(sql, dados)
            print(sql)
            print(result)
        connection.commit()
        print("COMMIT EXECUTADO COM SUCESSO!")

except pymysql.Error as e:
    print(f"Ocorreu um erro no MySQL: {e}")
    if connection:
        connection.rollback()  # Desfaz qualquer mudança que possa ter ocorrido
finally:
    if 'connection' in locals() and connection.open:
        connection.close()
