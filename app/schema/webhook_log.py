from pydantic import BaseModel
from datetime import datetime

class WebhookLogOut(BaseModel):
    id: str
    source: str
    payload: str
    timestamp: datetime

    class Config:
        from_attributes = True
