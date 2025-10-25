from sqlalchemy import Column, String, Float, DateTime
from datetime import datetime
from app.db import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(String, primary_key=True)
    user_id = Column(String)
    total = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
