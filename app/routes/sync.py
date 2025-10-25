from fastapi import APIRouter
from app.services.liquor_importer import fetch_liquors

router = APIRouter()

@router.post("/refresh")
async def refresh_products():
    data = await fetch_liquors()
    return {"updated": len(data), "items": data}
