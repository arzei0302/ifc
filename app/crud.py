from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from typing import List, Optional

from . import models, schemas

async def get_ifc_news(db: AsyncSession, news_id: int) -> Optional[models.IfcNews]:
    result = await db.execute(select(models.IfcNews).where(models.IfcNews.id == news_id))
    return result.scalar_one_or_none()

async def get_ifc_news_list(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[models.IfcNews]:
    result = await db.execute(select(models.IfcNews).offset(skip).limit(limit))
    return result.scalars().all()

async def create_ifc_news(db: AsyncSession, news: schemas.IfcNewsCreate) -> models.IfcNews:
    db_news = models.IfcNews(**news.dict())
    db.add(db_news)
    await db.commit()
    await db.refresh(db_news)
    return db_news

async def update_ifc_news(db: AsyncSession, news_id: int, news: schemas.IfcNewsUpdate) -> Optional[models.IfcNews]:
    db_news = await get_ifc_news(db, news_id)
    if not db_news:
        return None
    for key, value in news.dict().items():
        setattr(db_news, key, value)
    await db.commit()
    await db.refresh(db_news)
    return db_news

async def delete_ifc_news(db: AsyncSession, news_id: int) -> Optional[models.IfcNews]:
    db_news = await get_ifc_news(db, news_id)
    if not db_news:
        return None
    await db.delete(db_news)
    await db.commit()
    return db_news
