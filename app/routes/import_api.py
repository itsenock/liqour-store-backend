from fastapi import APIRouter, HTTPException
from app.db import SessionLocal
from app.models.liquor import Liquor
from app.services.normalize_openfood import parse_openfood_product
import httpx

router = APIRouter()

@router.post("/seed")
async def seed_liquors():
    async with httpx.AsyncClient() as client:
        res = await client.get("https://world.openfoodfacts.org/category/alcoholic-beverages.json")
        res.raise_for_status()
        products = res.json().get("products", [])

    db = SessionLocal()
    for product in products[:50]:  # Limit for performance
        parsed = parse_openfood_product(product)
        liquor = Liquor(**parsed)
        db.add(liquor)
    db.commit()
    db.close()
    return {"message": f"{len(products[:50])} liquors imported"}
