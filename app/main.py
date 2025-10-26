from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import Base, engine
from app.routes import (
    products, checkout, import_api, webhooks,
    dashboard, admin, orders, auth, status, users
)
from app.models import user  # ensures User table is created

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Liquor Store API",
    description="Backend for managing products, payments, orders, and imports",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(checkout.router, prefix="/checkout", tags=["Checkout"])
app.include_router(import_api.router, prefix="/import", tags=["Import"])
app.include_router(webhooks.router, prefix="/webhooks", tags=["Webhooks"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(status.router, prefix="/status", tags=["Health"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.on_event("startup")
async def startup_event():
    print("🚀 Liquor Store API is live and ready.")
