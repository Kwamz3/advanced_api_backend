from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    phone: str

    @field_validator('phone')
    def validate_phone(cls, value):
        if not value.isdigit():
            raise ValueError('Phone number must contain only digits')
        if len(value) != 10:
            raise ValueError('Phone number must be 10 digits long')
        return value