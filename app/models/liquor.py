from sqlalchemy import Column, String, Float
from app.db import Base

class Liquor(Base):
    __tablename__ = "liquors"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    subcategory = Column(String, nullable=False)
    abv = Column(Float, nullable=True)
    price = Column(Float, nullable=False)
    image = Column(String, nullable=True)
    description = Column(String, nullable=True)
