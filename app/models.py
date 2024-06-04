from sqlalchemy import Column, Integer, String, Text
from .database import Base

class IfcNews(Base):
    __tablename__ = "ifc_news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    text = Column(Text)
    image = Column(String)
    video = Column(String)
