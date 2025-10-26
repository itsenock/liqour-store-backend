from sqlalchemy import Column, String
from app.db import Base

class User(Base):
    __tablename__ = "users"

    uid = Column(String, primary_key=True, index=True)  # Firebase UID
    email = Column(String, nullable=False, index=True)
    name = Column(String, nullable=True)
    role = Column(String, default="user")  # user, admin, staff
    picture = Column(String, nullable=True)
