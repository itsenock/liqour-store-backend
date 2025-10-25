import base64
from datetime import datetime
import httpx
from app.core.config import MPESA_CONSUMER_KEY, MPESA_CONSUMER_SECRET, MPESA_SHORTCODE, MPESA_PASSKEY

def generate_password_and_timestamp():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    raw = MPESA_SHORTCODE + MPESA_PASSKEY + timestamp
    password = base64.b64encode(raw.encode()).decode()
    return password, timestamp

async def get_mpesa_token():
    async with httpx.AsyncClient() as client:
        res = await client.get(
            "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials",
            auth=(MPESA_CONSUMER_KEY, MPESA_CONSUMER_SECRET)
        )
        res.raise_for_status()
        return res.json()["access_token"]

async def initiate_mpesa_payment(phone: str, amount: float):
    token = await get_mpesa_token()
    password, timestamp = generate_password_and_timestamp()

    payload = {
        "BusinessShortCode": MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": MPESA_SHORTCODE,
        "PhoneNumber": phone,
        "CallBackURL": "https://your-backend.com/webhooks/mpesa/callback",
        "AccountReference": "LiquorStore",
        "TransactionDesc": "Liquor purchase"
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest",
            json=payload,
            headers=headers
        )
        res.raise_for_status()
        return res.json()
