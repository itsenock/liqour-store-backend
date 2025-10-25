from fastapi import APIRouter, Header, HTTPException
from app.core.firebase import verify_token
from app.schemas.user import UserProfile

router = APIRouter()

@router.get("/me", response_model=UserProfile)
def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")
    token = authorization.split(" ")[1]
    try:
        decoded = verify_token(token)
        return {
            "uid": decoded.get("uid"),
            "email": decoded.get("email"),
            "name": decoded.get("name"),
            "role": decoded.get("role", "user"),
            "picture": decoded.get("picture")
        }
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
