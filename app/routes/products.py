from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.core.firebase import get_user_role
from app.models.liquor import Liquor
from app.schema.liquor import LiquorCreate, LiquorResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/", response_model=list[LiquorResponse])
def get_liquors(db: Session = Depends(get_db)):
    return db.query(Liquor).all()

@router.post("/", response_model=LiquorResponse)
def create_liquor(data: LiquorCreate, db: Session = Depends(get_db), token: str = Header(...)):
    role = get_user_role(token)
    if role != "admin":
        return {"error": "Unauthorized"}
    liquor = Liquor(**data.dict())
    db.add(liquor)
    db.commit()
    return liquor
