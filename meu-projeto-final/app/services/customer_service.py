from mysql.connector.abstracts import MySQLConnectionAbstract
from fastapi import HTTPException
from app.models.customers import Customer


class CustomerServices:
    @staticmethod
    def get_customer(customer_id: int, db: MySQLConnectionAbstract):
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
        customer = cursor.fetchone()
        cursor.close()
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        return customer

    @staticmethod
    def create_customer(customer: Customer, db: MySQLConnectionAbstract):
        cursor = db.cursor()
        sql = "INSERT INTO customers (nome, idade) VALUES (%s, %s)"
        cursor.execute(sql, (customer.name, customer.age))
        db.commit()
        new_id = cursor.lastrowid
        cursor.close()
        return {"id": new_id, "message": "Customer created successfully",
                "data": customer}

    @staticmethod
    def update_customer(
        customer_id: int, updated_data: Customer, db: MySQLConnectionAbstract
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
            return {
                "message": "Customer updated successfully", "id": customer_id
            }

    @staticmethod
    def delete_customer(customer_id: int, db: MySQLConnectionAbstract):
        with db.cursor() as cursor:
            sql = "DELETE FROM customers WHERE id = %s"
            cursor.execute(sql, (customer_id,))
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Customer not "
                                    "found")
            db.commit()
            return {
                "message": "Customer deleted successfully", "id": customer_id
            }
