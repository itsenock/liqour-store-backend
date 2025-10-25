from fastapi import APIRouter, Header, Depends
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
        return {"error": "Unauthorized"}

    product_count = db.query(Liquor).count()
    tx_count = db.query(MpesaTransaction).count()
    revenue_sum = sum(tx.amount for tx in db.query(MpesaTransaction).with_entities(MpesaTransaction.amount).all())
    recent_tx = db.query(MpesaTransaction).order_by(MpesaTransaction.timestamp.desc()).limit(5).all()

    return {
        "products": product_count,
        "transactions": tx_count,
        "revenue": revenue_sum,
        "recent": [tx.reference for tx in recent_tx]
    }
