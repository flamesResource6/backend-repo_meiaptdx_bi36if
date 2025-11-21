"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class Consultation(BaseModel):
    """Consultation requests from the Contact page.
    Collection name: "consultation"
    """
    first_name: str = Field(..., min_length=1, max_length=100, description="Visitor first name")
    last_name: str = Field(..., min_length=1, max_length=100, description="Visitor last name")
    company: Optional[str] = Field(None, max_length=150, description="Company name (optional)")
    email: EmailStr = Field(..., description="Valid email address")
    country_code: str = Field(..., min_length=1, max_length=5, description="E.164 country code like +1, +44")
    phone_number: str = Field(..., min_length=4, max_length=20, description="Phone number without country code")
    message: Optional[str] = Field(None, max_length=2000, description="Optional message")

    class Config:
        json_schema_extra = {
            "example": {
                "first_name": "Aisha",
                "last_name": "Khan",
                "company": "DataNova AI",
                "email": "aisha.khan@example.com",
                "country_code": "+65",
                "phone_number": "81234567",
                "message": "Looking for a proof-of-concept on demand forecasting with our retail data."
            }
        }
