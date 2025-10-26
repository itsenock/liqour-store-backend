from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models.liquor import Liquor
from app.models.mpesa import MpesaTransaction

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def dashboard(db: Session = Depends(get_db)):
    product_count = db.query(Liquor).count()
    tx_count = db.query(MpesaTransaction).count()

    # More efficient revenue aggregation
    revenue_sum = db.query(MpesaTransaction).with_entities(
        MpesaTransaction.amount
    ).all()
    total_revenue = sum(tx.amount for tx in revenue_sum)

    recent_tx = db.query(MpesaTransaction).order_by(
        MpesaTransaction.timestamp.desc()
    ).limit(5).all()

    return {
        "total_products": product_count,
        "total_transactions": tx_count,
        "total_revenue": total_revenue,
        "recent_references": [tx.reference for tx in recent_tx]
    }
