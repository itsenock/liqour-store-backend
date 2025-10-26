from pydantic import BaseModel, Field
from datetime import datetime

class OrderCreate(BaseModel):
    user_id: str = Field(..., description="Firebase UID of the user")
    total: float = Field(..., description="Total amount of the order")

class OrderResponse(OrderCreate):
    id: str = Field(..., description="Order ID")
    timestamp: datetime = Field(..., description="Time the order was placed")

    class Config:
        from_attributes = True  # Pydantic v2 compatibility
