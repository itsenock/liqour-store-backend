import httpx
from app.core.config import FLUTTERWAVE_SECRET_KEY

async def initiate_bank_transfer(account: str, amount: float):
    async with httpx.AsyncClient() as client:
        headers = {
            "Authorization": f"Bearer {FLUTTERWAVE_SECRET_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "account_bank": "044",  # Bank code (e.g., KCB, Equity)
            "account_number": account,
            "amount": amount,
            "currency": "KES",
            "narration": "Liquor Store Purchase",
            "reference": "LIQ-" + account[-4:],  # Unique reference
            "beneficiary_name": "Customer"
        }
        res = await client.post("https://api.flutterwave.com/v3/transfers", json=payload, headers=headers)
        return res.json()
