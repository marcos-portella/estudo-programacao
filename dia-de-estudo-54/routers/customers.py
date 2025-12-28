from fastapi import APIRouter, HTTPException
from database import get_connection
from pydantic import BaseModel, Field

# Criamos o router. O "prefix" ajuda a não termos de escrever "/customers" em
# tudo
router = APIRouter(prefix="/customers", tags=["Customers"])


class Customer(BaseModel):
    name: str = Field(min_length=3, max_length=50,
                      examples=["Marcos Portella"])
    age: int = Field(gt=0, lt=120, examples=[25])


@router.get("/{customer_id}")
def get_customer(customer_id: int):
    connection = get_connection()

    # Cláusula de Guarda: Se a conexão for None, lança erro 500
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection "
                            "failed")

    try:
        with connection.cursor() as cursor:
            # Meu sql
            sql = "SELECT * FROM customers WHERE id = %s"
            cursor.execute(sql, (customer_id,))

            result = cursor.fetchone()

            if result is None:
                raise HTTPException(status_code=404, detail="Customer not "
                                    "found")
            return result

    finally:
        connection.close()


@router.post("/")  # Como o prefixo é "/customers", aqui basta "/"
def create_customer(customer: Customer):
    connection = get_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection "
                            "failed")
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO customers (nome, idade) VALUES (%s, %s)"
            cursor.execute(sql, (customer.name, customer.age))
        connection.commit()
        return {"message": "Customer created successfully"}
    finally:
        connection.close()


@router.put("/{customer_id}")
def update_customer(customer_id: int, customer: Customer):
    connection = get_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection "
                            "failed")
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE customers SET nome = %s, idade = %s WHERE id = %s"
            cursor.execute(sql, (customer.name, customer.age, customer_id))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Customer not "
                                    "found")
        connection.commit()
        return {"message": "Customer updated"}
    finally:
        connection.close()


@router.delete("/{customer_id}")
def delete_customer(customer_id: int):
    connection = get_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection "
                            "failed")
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM customers WHERE id = %s"
            cursor.execute(sql, (customer_id,))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Customer not "
                                    "found")
        connection.commit()
        return {"message": "Customer deleted"}
    finally:
        connection.close()
