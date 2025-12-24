import os
import pymysql
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()


# 1. Schema (The "Model")
class Customer(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=0, le=120)


# 2. Database Connection
def get_connection():
    return pymysql.connect(
        host=os.environ['MYSQL_HOST'],
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        database=os.environ['MYSQL_DATABASE'],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )


# 3. Routes (The "Endpoints")
@app.post("/customers")
def create_customer(customer: Customer):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO customers (nome, idade) VALUES (%s, %s)"
            cursor.execute(sql, (customer.name, customer.age))
        conn.commit()
        return {"message": f"Customer {customer.name} created successfully!"}
    finally:
        conn.close()


@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM customers WHERE id = %s"
            cursor.execute(sql, (customer_id,))

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Customer not "
                                                            "found")

        conn.commit()
        return {"message": f"Customer ID {customer_id} deleted successfully"}
    finally:
        conn.close()


@app.put("/customers/{customer_id}")
def update_customer(customer_id: int, customer: Customer):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # SQL para atualizar
            sql = "UPDATE customers SET nome = %s, idade = %s WHERE id = %s"
            cursor.execute(sql, (customer.name, customer.age, customer_id))

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Customer not "
                                    "found")

        connection.commit()
        return {"message": f"Customer ID {customer_id} updated successfully"}
    finally:
        connection.close()


@app.get("/customers/{customers_id}")
def get_customers(customer_id: int):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Meu sql
            sql = "SELECT * FROM customers WHERE id = %s"
            cursor.execute(sql, (customer_id,))

            result = cursor.fetchone()

            if result is None:
                raise HTTPException(status_code=404, detail="Customers not "
                                    "found")
            return result

    finally:
        connection.close()
