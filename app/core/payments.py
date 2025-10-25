from app.core.stripe import create_stripe_session
from app.core.mpesa import initiate_mpesa_payment
from app.core.paypal import create_paypal_order
from app.core.bank import initiate_bank_transfer

def route_payment(method: str, payload: dict):
    if method == "card":
        return create_stripe_session(payload["items"])
    elif method == "mpesa":
        return initiate_mpesa_payment(payload["phone"], payload["amount"])
    elif method == "paypal":
        return create_paypal_order(payload["items"])
    elif method == "bank":
        return initiate_bank_transfer(payload["account"], payload["amount"])
    else:
        raise ValueError("Unsupported payment method")
