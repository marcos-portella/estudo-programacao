from fastapi import APIRouter, Depends, HTTPException
from mysql.connector.abstracts import MySQLConnectionAbstract
from app.dependencies import get_db
from app.models.customers import Customer

router = APIRouter()


@router.get("/{customer_id}")
def get_customer(customer_id: int, db: MySQLConnectionAbstract =
                 Depends(get_db)):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
    customer = cursor.fetchone()
    cursor.close()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer
    # Ao chegar aqui, o FastAPI volta no 'get_db' e fecha a conexão para você.


@router.post("/")
def create_customer(
    customer: Customer, db: MySQLConnectionAbstract = Depends(get_db)
):
    cursor = db.cursor()
    sql = "INSERT INTO customers (nome, idade) VALUES (%s, %s)"
    cursor.execute(sql, (customer.name, customer.age))
    db.commit()  # O commit deve ser feito aqui após o sucesso da query
    new_id = cursor.lastrowid
    cursor.close()
    return {"id": new_id, "message": "Customer created successfully",
            "data": customer}


@router.put("/{customer_id}")
def update_customer(
    customer_id: int, updated_data: Customer,
    db: MySQLConnectionAbstract = Depends(get_db)
):
    with db.cursor() as cursor:
        sql = "UPDATE customers SET nome = %s, idade = %s WHERE id = %s"
        cursor.execute(
            sql, (updated_data.name, updated_data.age, customer_id)
        )
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Customer not "
                                "found")
        db.commit()
        return {"message": "Customer updated successfully", "id": customer_id}


@router.delete("/{customer_id}")
def delete_customer(
    customer_id: int, db: MySQLConnectionAbstract = Depends(get_db)
):
    with db.cursor() as cursor:
        sql = "DELETE FROM customers WHERE id = %s"
        cursor.execute(sql, (customer_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Customer not "
                                "found")
        db.commit()
        return {"message": "Customer deleted successfully", "id": customer_id}
