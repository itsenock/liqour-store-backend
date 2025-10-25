from sqlalchemy import Column, String, Float, DateTime
from datetime import datetime
from app.db import Base

class MpesaTransaction(Base):
    __tablename__ = "mpesa_transactions"
    id = Column(String, primary_key=True, index=True)
    phone = Column(String)
    amount = Column(Float)
    reference = Column(String)
    status = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
