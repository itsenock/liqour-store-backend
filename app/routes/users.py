from fastapi import APIRouter, Header
from app.core.firebase import verify_token

router = APIRouter()

@router.get("/me")
def get_current_user(token: str = Header(...)):
    try:
        decoded = verify_token(token)
        return {
            "uid": decoded.get("uid"),
            "email": decoded.get("email"),
            "name": decoded.get("name"),
            "role": decoded.get("role", "user"),
            "picture": decoded.get("picture")
        }
    except Exception as e:
        return {"error": "Invalid token", "details": str(e)}
