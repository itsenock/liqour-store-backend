from pydantic import BaseModel

class LiquorCreate(BaseModel):
    name: str
    category: str
    subcategory: str
    abv: float
    price: float
    image: str
    description: str

class LiquorResponse(LiquorCreate):
    id: str
