from sqlalchemy import Column, String, Float, Text
from app.db import Base

class Liquor(Base):
    __tablename__ = "liquors"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    abv = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    image = Column(String, nullable=False)
    description = Column(Text, nullable=True)
