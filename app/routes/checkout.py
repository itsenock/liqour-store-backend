from fastapi import APIRouter, BackgroundTasks, Header
from app.core.twilio_sms import send_sms
from app.core.email import send_email
from app.core.firebase import get_user_role
from app.core.stripe import create_checkout_session

router = APIRouter()

@router.post("/")
def checkout(payload: dict, background: BackgroundTasks, token: str = Header(...)):
    role = get_user_role(token)
    if role not in ["admin", "user"]:
        return {"error": "Unauthorized"}

    background.add_task(send_sms, payload["phone"], "Thank you for your purchase!")
    background.add_task(send_email, payload["email"], "Order Confirmation", "Your order has been received and is being processed.")
    url = create_checkout_session(payload["items"])
    return {"checkout_url": url}
