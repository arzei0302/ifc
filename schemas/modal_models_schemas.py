from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional

class ConsultationRequestSchema(BaseModel):
    full_name: str = Field(..., max_length=100)
    phone_number: str = Field(..., max_length=20)
    agree_to_privacy_policy: bool
    created_at: datetime

class PartnershipRequestSchema(BaseModel):
    contact_person: str = Field(..., max_length=100)
    phone_number: str = Field(..., max_length=20)
    region: str = Field(..., max_length=100)
    product_group: str = Field(..., max_length=100)
    agree_to_privacy_policy: bool
    created_at: datetime

class JobApplicationSchema(BaseModel):
    name: str = Field(..., max_length=100)
    phone: str = Field(..., max_length=20)
    email: EmailStr
    position: str = Field(..., max_length=100)
    created_at: datetime
    attachment: Optional[bytes]  

class QuestionRequestSchema(BaseModel):
    name: str = Field(..., max_length=100)
    phone: str = Field(..., max_length=20)
    email: EmailStr
    message: str
    created_at: datetime
    attachment: Optional[bytes] 

class MudarabaCalculatorSchema(BaseModel):
    deposit_type: str = Field(..., max_length=100)
    amount: int
    term: int

class GeneralRequestSchema(BaseModel):
    full_name: str = Field(..., max_length=100)
    phone_number: str = Field(..., max_length=20)
    email: EmailStr
    agree_to_privacy_policy: bool
    created_at: datetime
