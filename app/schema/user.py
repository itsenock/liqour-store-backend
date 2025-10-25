from pydantic import BaseModel
from typing import Optional

class UserProfile(BaseModel):
    uid: str
    email: Optional[str]
    name: Optional[str]
    role: str
    picture: Optional[str]
