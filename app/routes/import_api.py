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
    imported = 0

    for product in products[:50]:  # Limit for performance
        try:
            parsed = parse_openfood_product(product)
            if not parsed or not parsed.get("id"):
                continue

            # Avoid duplicates
            if db.query(Liquor).filter(Liquor.id == parsed["id"]).first():
                continue

            liquor = Liquor(**parsed)
            db.add(liquor)
            imported += 1
        except Exception as e:
            print(f"Skipping product due to error: {e}")

    db.commit()
    db.close()

    return {"message": f"{imported} liquors imported"}
