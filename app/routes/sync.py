from fastapi import APIRouter, HTTPException
from app.services.liquor_importer import fetch_liquors

router = APIRouter()

@router.post("/refresh")
async def refresh_products():
    try:
        data = await fetch_liquors()
        return {
            "updated": len(data),
            "items": data  # You can trim or summarize if needed
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to refresh products: {str(e)}")
