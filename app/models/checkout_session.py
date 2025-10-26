from sqlalchemy import Column, String, DateTime
from datetime import datetime
from app.db import Base

class CheckoutSession(Base):
    __tablename__ = "checkout_sessions"

    id = Column(String, primary_key=True)  # Stripe session ID
    user_id = Column(String)
    status = Column(String, default="pending")  # pending, completed, failed
    expires_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
