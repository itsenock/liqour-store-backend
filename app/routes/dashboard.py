from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models.liquor import Liquor
from app.models.mpesa import MpesaTransaction

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/")
def dashboard(db: Session = Depends(get_db)):
    product_count = db.query(Liquor).count()
    tx_count = db.query(MpesaTransaction).count()
    total_revenue = db.query(MpesaTransaction).with_entities(MpesaTransaction.amount).all()
    revenue_sum = sum(tx.amount for tx in total_revenue)

    recent_tx = db.query(MpesaTransaction).order_by(MpesaTransaction.timestamp.desc()).limit(5).all()

    return {
        "products": product_count,
        "transactions": tx_count,
        "revenue": revenue_sum,
        "recent": [tx.reference for tx in recent_tx]
    }
