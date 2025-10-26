from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.core.firebase import get_user_role
from app.models.liquor import Liquor
from app.schema.liquor import LiquorCreate, LiquorResponse
import uuid

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[LiquorResponse])
def get_liquors(category: str = None, db: Session = Depends(get_db)):
    query = db.query(Liquor)
    if category:
        query = query.filter(Liquor.category.ilike(f"%{category}%"))
    return query.order_by(Liquor.name.asc()).all()

@router.get("/{liquor_id}", response_model=LiquorResponse)
def get_liquor(liquor_id: str, db: Session = Depends(get_db)):
    liquor = db.query(Liquor).filter(Liquor.id == liquor_id).first()
    if not liquor:
        raise HTTPException(status_code=404, detail="Product not found")
    return liquor

@router.post("/", response_model=LiquorResponse)
def create_liquor(
    data: LiquorCreate,
    db: Session = Depends(get_db),
    token: str = Header(...)
):
    role = get_user_role(token)
    if role != "admin":
        raise HTTPException(status_code=403, detail="Unauthorized")

    liquor = Liquor(
        id=str(uuid.uuid4()),
        name=data.name,
        category=data.category,
        abv=data.abv,
        price=data.price,
        image=data.image,
        description=data.description
    )
    db.add(liquor)
    db.commit()
    db.refresh(liquor)
    return liquor
