from sqlalchemy import Column, String, Text, DateTime
from datetime import datetime
from app.db import Base

class WebhookLog(Base):
    __tablename__ = "webhook_logs"

    id = Column(String, primary_key=True)
    source = Column(String)  # stripe, paypal, mpesa
    payload = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
