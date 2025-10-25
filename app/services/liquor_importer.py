import httpx
from app.core.config import LIQUOR_API_URL, LIQUOR_API_KEY

async def fetch_liquors():
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{LIQUOR_API_URL}?key={LIQUOR_API_KEY}")
        res.raise_for_status()
        return res.json()
