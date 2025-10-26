from pydantic import BaseModel

class CategoryOut(BaseModel):
    id: str
    name: str

    class Config:
        from_attributes = True
