import stripe
from app.core.config import settings  # ✅ Import the settings object


stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(items: list[dict]) -> str:
    line_items = [
        {
            "price_data": {
                "currency": "usd",
                "product_data": {"name": item["name"]},
                "unit_amount": int(item["price"] * 100),
            },
            "quantity": item["quantity"],
        }
        for item in items
    ]
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url="https://your-frontend.com/success",
        cancel_url="https://your-frontend.com/cancel",
    )
    return session.url
