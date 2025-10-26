from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserProfile(BaseModel):
    uid: str = Field(..., description="Firebase UID of the user")
    email: Optional[str] = Field(None, description="User's email address")
    name: Optional[str] = Field(None, description="User's display name")
    role: str = Field("user", description="User role, defaults to 'user'")
    picture: Optional[str] = Field(None, description="URL to user's profile picture")
    phone_number: Optional[str] = Field(None, description="User's phone number if available")
    provider_id: Optional[str] = Field(None, description="Auth provider ID (e.g. google.com, password)")

    class Config:
        from_attributes = True  # ✅ Pydantic v2 replacement for orm_mode

class UserCreate(BaseModel):
    uid: str = Field(..., description="Firebase UID")
    email: Optional[str] = Field(None, description="User's email address")
    name: Optional[str] = Field(None, description="User's display name")
    role: str = Field("user", description="User role, defaults to 'user'")
    picture: Optional[str] = Field(None, description="URL to user's profile picture")
    phone_number: Optional[str] = Field(None, description="User's phone number if available")
    provider_id: Optional[str] = Field(None, description="Auth provider ID (e.g. google.com, password)")

class UserOut(UserProfile):
    created_at: Optional[datetime] = Field(None, description="Timestamp when the user was created")

    class Config:
        from_attributes = True
