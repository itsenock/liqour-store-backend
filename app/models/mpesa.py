from sqlalchemy import Column, String, Float, DateTime
from datetime import datetime
from app.db import Base

class MpesaTransaction(Base):
    __tablename__ = "mpesa_transactions"

    id = Column(String, primary_key=True, index=True)  # Transaction ID from M-Pesa
    phone = Column(String, nullable=False, index=True)  # Customer phone number
    amount = Column(Float, nullable=False)  # Amount paid
    reference = Column(String, nullable=False, index=True)  # M-Pesa reference code
    status = Column(String, nullable=False, default="pending")  # Payment status
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)  # Time of transaction
