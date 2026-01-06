from fastapi import APIRouter, Depends
from mysql.connector.abstracts import MySQLConnectionAbstract
from app.dependencies.database import get_db
from app.dependencies.auth import get_api_key
from app.models.orders import Order, OrderUpdate, DashboardStats
from typing import Optional
from app.services.order_service import OrderService

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    dependencies=[Depends(get_api_key)]
)


@router.post("/")
def create_order(order: Order, db: MySQLConnectionAbstract = Depends(get_db)):
    return OrderService.create_order(order, db)


@router.get("/")
def get_orders(
    customer_id: Optional[int] = None,
    db: MySQLConnectionAbstract = Depends(get_db)
):
    return OrderService.list_orders(db, customer_id)


@router.put("/{order_id}")
def update_order(
    order_id: int, order_data: OrderUpdate,
    db: MySQLConnectionAbstract = Depends(get_db)
):
    return OrderService.update_order(order_id, order_data, db)


@router.get("/stats", response_model=DashboardStats)
def get_order_stats(db: MySQLConnectionAbstract = Depends(get_db)):
    return OrderService.get_order_stats(db)
