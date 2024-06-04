from pydantic import BaseModel
from typing import Optional

class IfcNewsBase(BaseModel):
    title: str
    text: str
    image: Optional[str] = None
    video: Optional[str] = None

class IfcNewsCreate(IfcNewsBase):
    pass

class IfcNewsUpdate(IfcNewsBase):
    pass

class IfcNewsInDBBase(IfcNewsBase):
    id: int

    class Config:
        from_attributes = True  # Изменено orm_mode на from_attributes

class IfcNews(IfcNewsInDBBase):
    pass

class IfcNewsInDB(IfcNewsInDBBase):
    pass

