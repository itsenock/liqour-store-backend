from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.services.liquor_importer import fetch_liquors
from app.models.liquor import Liquor
from app.core.firebase import get_user_role

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/")
async def import_liquors(db: Session = Depends(get_db), token: str = Header(...)):
    role = get_user_role(token)
    if role != "admin":
        return {"error": "Unauthorized"}
    data = await fetch_liquors()
    for item in data:
        liquor = Liquor(**item)
        db.merge(liquor)
    db.commit()
    return {"imported": len(data)}
