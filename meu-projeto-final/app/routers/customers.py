from fastapi import APIRouter, Depends
from mysql.connector.abstracts import MySQLConnectionAbstract
from app.dependencies.database import get_db
from app.dependencies.auth import get_api_key
from app.models.customers import Customer
from app.services.customer_service import CustomerServices

router = APIRouter(
    prefix="/customers",
    tags=["customers"],
    dependencies=[Depends(get_api_key)]  # Tranca TODAS as rotas deste arquivo
    # de uma vez!
)


@router.get("/{customer_id}")
def get_customer(
    customer_id: int, db: MySQLConnectionAbstract = Depends(get_db)
):
    return CustomerServices.get_customer(customer_id, db)


@router.post("/")
def create_customer(
    customer: Customer, db: MySQLConnectionAbstract = Depends(get_db)
):
    return CustomerServices.create_customer(customer, db)


@router.put("/{customer_id}")
def update_customer(
    customer_id: int, updated_data: Customer,
    db: MySQLConnectionAbstract = Depends(get_db)
):
    return CustomerServices.update_customer(customer_id, updated_data, db)


@router.delete("/{customer_id}")
def delete_customer(
    customer_id: int, db: MySQLConnectionAbstract = Depends(get_db)
):
    return CustomerServices.delete_customer(customer_id, db)
