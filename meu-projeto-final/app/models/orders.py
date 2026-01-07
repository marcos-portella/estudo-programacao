from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class Order(BaseModel):
    description: str
    amount: float = Field(
        gt=0, description="O valor do pedido deve ser positivo"
    )
    customer_id: int
    pass


class OrderResponse(Order):
    id: int
    created_at: datetime
    customer_name: str

    model_config = ConfigDict(from_attributes=True)


class OrderUpdate(BaseModel):
    description: str
    amount: float


class DashboardStats(BaseModel):
    total_orders: int
    total_revenue: float
    average_order_value: float
