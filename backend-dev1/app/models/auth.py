from pydantic import BaseModel, Field, EmailStr



class EmailRequest(BaseModel):
    email: EmailStr = Field(..., examples=["user@example.com"])

class OTPVerifyRequest(BaseModel):
    email: EmailStr = Field(..., examples=["user@example.com"])
    otp: str = Field(..., min_length=4, max_length=8, examples=["123456"])

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: dict

class OTPResponse(BaseModel):
    message: str
    email: str
    expires_in_minutes: int