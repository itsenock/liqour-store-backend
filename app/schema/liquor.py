from pydantic import BaseModel, Field
from typing import Optional

class LiquorBase(BaseModel):
    name: str = Field(..., description="Name of the liquor")
    category: str = Field(..., description="Category or type of liquor")
    abv: float = Field(..., description="Alcohol by volume percentage")
    price: float = Field(..., description="Price of the liquor")
    image: str = Field(..., description="URL to the liquor image")
    description: Optional[str] = Field(None, description="Optional description of the liquor")

class LiquorCreate(LiquorBase):
    pass  # No ID required from client — generated server-side

class LiquorResponse(LiquorBase):
    id: str = Field(..., description="Unique identifier for the liquor")

    class Config:
        from_attributes = True  # ✅ Pydantic v2 replacement for orm_mode
