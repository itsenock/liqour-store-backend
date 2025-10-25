from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models.order import Order
import uuid

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/")
def create_order(payload: dict, db: Session = Depends(get_db)):
    order = Order(id=str(uuid.uuid4()), user_id=payload["user"], total=payload["total"])
    db.add(order)
    db.commit()
    return order
