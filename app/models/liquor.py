from sqlalchemy import Column, String, Float
from app.db import Base

class Liquor(Base):
    __tablename__ = "liquors"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    category = Column(String)
    abv = Column(Float)
    price = Column(Float)
    image = Column(String)
    description = Column(String)
