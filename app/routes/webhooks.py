from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models.mpesa import MpesaTransaction
import uuid

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/mpesa/callback")
async def mpesa_callback(request: Request, db: Session = Depends(get_db)):
    try:
        data = await request.json()
        stk = data["Body"]["stkCallback"]
        result_code = stk["ResultCode"]
        result_desc = stk["ResultDesc"]
        metadata = stk.get("CallbackMetadata", {}).get("Item", [])

        phone = next((i["Value"] for i in metadata if i["Name"] == "PhoneNumber"), None)
        amount = next((i["Value"] for i in metadata if i["Name"] == "Amount"), None)
        ref = next((i["Value"] for i in metadata if i["Name"] == "MpesaReceiptNumber"), None)

        tx = MpesaTransaction(
            id=str(uuid.uuid4()),
            phone=phone or "unknown",
            amount=amount or 0,
            reference=ref or "none",
            status="Success" if result_code == 0 else f"Failed: {result_desc}"
        )
        db.add(tx)
        db.commit()
        db.refresh(tx)

        return {"status": "logged", "reference": tx.reference}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Callback error: {str(e)}")

@router.post("/stripe/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    print("Stripe Webhook:", payload.decode())  # Replace with signature verification later
    return {"status": "received"}

@router.post("/paypal/webhook")
async def paypal_webhook(request: Request):
    try:
        data = await request.json()
        print("PayPal Webhook:", data)  # Replace with signature verification later
        return {"status": "received"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Webhook error: {str(e)}")
