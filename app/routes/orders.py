from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models.order import Order
from app.schema.order import OrderCreate, OrderResponse
import uuid

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/", response_model=OrderResponse)
def create_order(payload: OrderCreate, db: Session = Depends(get_db)):
    try:
        order = Order(id=str(uuid.uuid4()), user_id=payload.user_id, total=payload.total)
        db.add(order)
        db.commit()
        db.refresh(order)
        return order
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Order creation failed: {str(e)}")
