from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/status")
def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat()
    }
