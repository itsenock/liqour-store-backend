from pydantic import BaseModel

class OrderItemCreate(BaseModel):
    liquor_id: str
    quantity: int
    unit_price: float

class OrderItemResponse(OrderItemCreate):
    id: str
    order_id: str

    class Config:
        from_attributes = True
