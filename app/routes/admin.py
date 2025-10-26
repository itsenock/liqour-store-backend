from fastapi import APIRouter, Header, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.core.firebase import get_user_role
from app.models.liquor import Liquor
from app.models.mpesa import MpesaTransaction

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/dashboard")
def admin_dashboard(token: str = Header(...), db: Session = Depends(get_db)):
    role = get_user_role(token)
    if role != "admin":
        raise HTTPException(status_code=403, detail="Unauthorized")

    product_count = db.query(Liquor).count()
    tx_count = db.query(MpesaTransaction).count()
    revenue_sum = sum(tx.amount for tx in db.query(MpesaTransaction).with_entities(MpesaTransaction.amount).all())
    recent_tx = db.query(MpesaTransaction).order_by(MpesaTransaction.timestamp.desc()).limit(5).all()

    return {
        "total_products": product_count,
        "total_transactions": tx_count,
        "total_revenue": revenue_sum,
        "recent_references": [tx.reference for tx in recent_tx]
    }
