from fastapi import APIRouter, Depends
from mysql.connector.abstracts import MySQLConnectionAbstract
from app.dependencies.database import get_db
from app.models.customers import Customer
from app.services.customer_service import CustomerServices
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/customers",
    tags=["customers"],
)


@router.get("/{customer_id}")
def get_customer(
    customer_id: int, db: MySQLConnectionAbstract = Depends(get_db),
    user_email: str = Depends(get_current_user)
):
    return CustomerServices.get_customer(customer_id, db, user_email)


@router.post("/")
def create_customer(
    customer: Customer, db: MySQLConnectionAbstract = Depends(get_db),
    user_email: str = Depends(get_current_user)
):
    return CustomerServices.create_customer(customer, db, user_email)


@router.put("/{customer_id}")
def update_customer(
    customer_id: int, updated_data: Customer,
    db: MySQLConnectionAbstract = Depends(get_db),
    user_email: str = Depends(get_current_user)
):
    return CustomerServices.update_customer(
        customer_id, updated_data, db, user_email
    )


@router.delete("/{customer_id}")
def delete_customer(
    customer_id: int,
    db: MySQLConnectionAbstract = Depends(get_db),
    user_email: str = Depends(get_current_user)  # <--- A TRANCA ESTÁ AQUI!
):
    # Agora, além de deletar, você sabe QUEM pediu para deletar (user_email)
    print(
        f"Usuário {user_email} está tentando deletar o cliente {customer_id}"
    )
    return CustomerServices.delete_customer(customer_id, db, user_email)
