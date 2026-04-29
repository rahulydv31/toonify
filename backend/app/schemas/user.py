"""
Pydantic schemas for User authentication
"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


# ✅ Keep base simple
class UserBase(BaseModel):
    email: EmailStr
    username: str
    full_name: Optional[str] = None


# ✅ REMOVE all validators (main cause of 422)
class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    username: str  # Can be username or email
    password: str


class UserResponse(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    created_at: datetime

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: UserResponse


class TokenRefresh(BaseModel):
    refresh_token: str


# ✅ simplify password change also
class PasswordChange(BaseModel):
    old_password: str
    new_password: str


class PasswordReset(BaseModel):
    email: EmailStr


class MessageResponse(BaseModel):
    message: str
    success: bool = True