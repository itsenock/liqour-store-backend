from fastapi import FastAPI
from app.routes import products, checkout, import_api, webhooks
from app.db import Base, engine
from app.models.mpesa import MpesaTransaction
from app.routes import dashboard
from app.routes import admin


# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Liquor Store API",
    description="Backend for managing products, payments, and imports",
    version="1.0.0"
)

# Register routes
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(checkout.router, prefix="/checkout", tags=["Checkout"])
app.include_router(import_api.router, prefix="/import", tags=["Import"])
app.include_router(webhooks.router, prefix="/webhooks", tags=["Webhooks"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])


