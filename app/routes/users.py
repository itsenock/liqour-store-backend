from fastapi import APIRouter, Header, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.firebase import verify_token
from app.schema.user import UserProfile
from app.models.user import User
from app.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/me", response_model=UserProfile)
def get_current_user(authorization: str = Header(...), db: Session = Depends(get_db)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")

    token = authorization.split(" ")[1]
    try:
        decoded = verify_token(token)
        uid = decoded.get("uid")
        email = decoded.get("email")

        # Sync user into DB if not exists
        user = db.query(User).filter_by(uid=uid).first()
        if not user:
            user = User(
                uid=uid,
                email=email,
                name=decoded.get("name"),
                role=decoded.get("role", "user"),
                picture=decoded.get("picture"),
                phone_number=decoded.get("phone_number"),
                provider_id=decoded.get("firebase", {}).get("sign_in_provider")
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        return user

    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Invalid or expired token: {str(e)}")
