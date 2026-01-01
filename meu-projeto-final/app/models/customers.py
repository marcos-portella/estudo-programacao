from pydantic import BaseModel, Field


class Customer(BaseModel):
    name: str = Field(..., min_length=1)
    age: int = Field(..., ge=0)
