from fastapi import APIRouter, BackgroundTasks, Header, HTTPException
from app.core.twilio_sms import send_sms
from app.core.email import send_email
from app.core.firebase import get_user_role
from app.core.stripe import create_checkout_session
from app.schema.checkout import CheckoutPayload

router = APIRouter()

@router.post("/", response_model=dict)
def checkout(
    payload: CheckoutPayload,
    background: BackgroundTasks,
    token: str = Header(...)
):
    role = get_user_role(token)
    if role not in ["admin", "user"]:
        raise HTTPException(status_code=403, detail="Unauthorized")

    background.add_task(send_sms, payload.phone, "Thank you for your purchase!")
    background.add_task(
        send_email,
        payload.email,
        "Order Confirmation",
        "Your order has been received and is being processed."
    )

    url = create_checkout_session(payload.items)
    return {"checkout_url": url}
