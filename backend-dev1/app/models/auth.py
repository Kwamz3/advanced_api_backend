from pydantic import BaseModel, Field, field_validator
import re





class PhoneNumberRequest(BaseModel):
    phone: str = Field(..., examples=["+233547688745"])
    
    @field_validator('phone')
    def validate_phone(cls, v):
        # Remove spaces and dashes
        phone = v.replace(" ", "").replace("-", "")
        # Basic validation for international format
        if not re.match(r'^\+?[1-9]\d{1,14}$', phone):
            raise ValueError('Invalid phone number format. Use international format (e.g., +233547688745)')
        return phone

class OTPVerifyRequest(BaseModel):
    phone: str = Field(..., examples=["+233547688745"])
    otp: str = Field(..., min_length=4, max_length=8, examples=["123456"])
    
    @field_validator('phone')
    def validate_phone(cls, v):
        phone = v.replace(" ", "").replace("-", "")
        if not re.match(r'^\+?[1-9]\d{1,14}$', phone):
            raise ValueError('Invalid phone number format')
        return phone

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: dict

class OTPResponse(BaseModel):
    message: str
    phone: str
    expires_in_minutes: int