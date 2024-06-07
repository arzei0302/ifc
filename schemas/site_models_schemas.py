from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class VacancySchema(BaseModel):
    title: str = Field(..., max_length=100)
    description: str
    image_url: Optional[str] = Field(None, max_length=255)
    created_at: datetime

class ContactSchema(BaseModel):
    branches: Optional[str]
    funding_points: Optional[str]
    phone_number: str = Field(..., max_length=20)

class ProductSchema(BaseModel):
    title: str = Field(..., max_length=100)
    description: str
    image_url: Optional[str] = Field(None, max_length=255)
    created_at: datetime

class PartnerSchema(BaseModel):
    title: str = Field(..., max_length=100)
    description: str
    image_url: Optional[str] = Field(None, max_length=255)
    video_url: Optional[str] = Field(None, max_length=255)
    created_at: datetime

class ShariaCouncilSchema(BaseModel):
    fullname: str = Field(..., max_length=100)
    description: str
    image_url: Optional[str] = Field(None, max_length=255)
    created_at: datetime

class NewsSchema(BaseModel):
    title: str = Field(..., max_length=100)
    text: str
    image_url: Optional[str] = Field(None, max_length=255)
    video_url: Optional[str] = Field(None, max_length=255)
    created_at: datetime

class AboutUsSchema(BaseModel):
    title: str = Field(..., max_length=100)
    description: str
    image_url: Optional[str] = Field(None, max_length=255)
    video_url: Optional[str] = Field(None, max_length=255)

class CenterBannerSchema(BaseModel):
    title: str = Field(..., max_length=100)
    description: Optional[str]
    image_url: Optional[str] = Field(None, max_length=255)

class FinancialReportSchema(BaseModel):
    title: str
    description: Optional[str]
    file_url: str
    created_at: datetime

class ProfitNormSchema(BaseModel):
    title: str
    description: Optional[str]
    file_url: str
    created_at: datetime
