from pydantic import BaseModel

class LiquorBase(BaseModel):
    name: str
    category: str
    abv: float
    price: float
    image: str
    description: str | None = None

class LiquorCreate(LiquorBase):
    id: str

class LiquorResponse(LiquorBase):
    id: str

    class Config:
        orm_mode = True
