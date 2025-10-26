from sqlalchemy import Column, String, Float, Integer, ForeignKey
from app.db import Base

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(String, primary_key=True)
    order_id = Column(String, ForeignKey("orders.id"))
    liquor_id = Column(String, ForeignKey("liquors.id"))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
