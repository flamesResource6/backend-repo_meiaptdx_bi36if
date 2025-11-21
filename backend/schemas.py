from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Consultation(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    company: Optional[str] = Field(None, max_length=150)
    email: EmailStr
    country_code: str = Field(..., min_length=1, max_length=5, description="E.164 country calling code, e.g., +1")
    phone_number: str = Field(..., min_length=4, max_length=20)
    message: Optional[str] = Field(None, max_length=2000)

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Jane",
                "last_name": "Doe",
                "company": "Acme AI",
                "email": "jane.doe@example.com",
                "country_code": "+1",
                "phone_number": "4155551234",
                "message": "We are looking for help with AI-driven analytics."
            }
        }
