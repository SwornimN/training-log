from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class SessionCreate(BaseModel):
    date: datetime
    duration_minutes: int
    notes: Optional[str] = None
    techniques: Optional[str] = None
    training_partner: Optional[str] = None

class SessionResponse(SessionCreate):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True