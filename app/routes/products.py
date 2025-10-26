from fastapi import APIRouter, Depends, Header, HTTPException, Query
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.core.firebase import get_user_role
from app.models.liquor import Liquor
from app.schema.liquor import LiquorCreate, LiquorResponse
from typing import Optional
import uuid

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[LiquorResponse])
def get_liquors(
    search: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    subcategory: Optional[str] = Query(None),
    sort: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Liquor)

    if search:
        query = query.filter(Liquor.name.ilike(f"%{search}%"))
    if category:
        query = query.filter(Liquor.category == category)
    if subcategory:
        query = query.filter(Liquor.subcategory == subcategory)
    if sort == "asc":
        query = query.order_by(Liquor.price.asc())
    elif sort == "desc":
        query = query.order_by(Liquor.price.desc())

    return query.all()

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
        subcategory=data.subcategory,
        abv=data.abv,
        price=data.price,
        image=data.image,
        description=data.description
    )
    db.add(liquor)
    db.commit()
    db.refresh(liquor)
    return liquor
