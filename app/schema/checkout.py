from pydantic import BaseModel, Field
from typing import List

class CheckoutItem(BaseModel):
    name: str = Field(..., description="Name of the item")
    price: float = Field(..., description="Unit price of the item")
    quantity: int = Field(..., description="Quantity being purchased")

class CheckoutPayload(BaseModel):
    phone: str = Field(..., description="Customer's phone number")
    email: str = Field(..., description="Customer's email address")
    items: List[CheckoutItem] = Field(..., description="List of items to purchase")
