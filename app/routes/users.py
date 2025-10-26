from fastapi import APIRouter, Header, HTTPException
from app.core.firebase import verify_token
from app.schema.user import UserProfile

router = APIRouter()

@router.get("/me", response_model=UserProfile)
def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")

    token = authorization.split(" ")[1]
    try:
        decoded = verify_token(token)
        return UserProfile(
            uid=decoded.get("uid"),
            email=decoded.get("email"),
            name=decoded.get("name"),
            role=decoded.get("role", "user"),
            picture=decoded.get("picture"),
            phone_number=decoded.get("phone_number"),
            provider_id=decoded.get("firebase", {}).get("sign_in_provider")
        )
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Invalid or expired token: {str(e)}")
