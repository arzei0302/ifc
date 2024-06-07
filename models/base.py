from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr

from core.config import settings
from utils import camel_case_to_snake_case


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )
    special_cases = {
       "News": "news",
       "ShariaCouncil": "sharia_council",
       "Vacancy": "vacancies",
       "AboutUs": "about_us",
       "CenterBanner": "center_banners"
    }

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{camel_case_to_snake_case(cls.__name__)}s"





    

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.special_cases.get(cls.__name__, camel_case_to_snake_case(cls.__name__) + 's')