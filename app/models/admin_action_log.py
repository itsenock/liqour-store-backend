from sqlalchemy import Column, String, DateTime, Text
from datetime import datetime
from app.db import Base

class AdminActionLog(Base):
    __tablename__ = "admin_action_logs"

    id = Column(String, primary_key=True)
    admin_id = Column(String)  # Firebase UID
    action = Column(String)  # e.g. "delete_product", "import_liquors"
    details = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
