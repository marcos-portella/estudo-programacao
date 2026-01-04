from pydantic import BaseModel
from datetime import datetime


class Order(BaseModel):
    description: str
    amount: float
    customer_id: int


class OrderResponse(Order):
    id: int
    created_at: datetime
    customer_name: str

    class Config:
        from_attributes = True


class OrderUpdate(BaseModel):
    description: str
    amount: float


class DashboardStats(BaseModel):
    total_orders: int
    total_revenue: float
    average_order_value: float
