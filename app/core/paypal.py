import httpx
from app.core.config import PAYPAL_CLIENT_ID, PAYPAL_SECRET

async def create_paypal_order(items: list):
    async with httpx.AsyncClient() as client:
        # Get access token
        res = await client.post(
            "https://api-m.sandbox.paypal.com/v1/oauth2/token",
            data={"grant_type": "client_credentials"},
            auth=(PAYPAL_CLIENT_ID, PAYPAL_SECRET)
        )
        token = res.json()["access_token"]

        # Create order
        payload = {
            "intent": "CAPTURE",
            "purchase_units": [{
                "amount": {
                    "currency_code": "USD",
                    "value": str(sum(item["price"] * item["quantity"] for item in items))
                }
            }]
        }
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        order = await client.post("https://api-m.sandbox.paypal.com/v2/checkout/orders", json=payload, headers=headers)
        return order.json()
