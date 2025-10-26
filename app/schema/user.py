from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserProfile(BaseModel):
    uid: str = Field(..., description="Firebase UID of the user")
    email: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    role: str = Field("user")
    picture: Optional[str] = Field(None)
    phone_number: Optional[str] = Field(None)
    provider_id: Optional[str] = Field(None)

    class Config:
        from_attributes = True

class UserCreate(UserProfile):
    pass

class UserOut(UserProfile):
    created_at: Optional[datetime] = Field(None)

    class Config:
        from_attributes = True
