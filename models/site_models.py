from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, DateTime, func
from .base import Base
from .int_id_pk import IntIdMixin


class Vacancy(Base, IntIdMixin):
    title_en: Mapped[str] = mapped_column(String(100), nullable=False)
    title_kg: Mapped[str] = mapped_column(String(100), nullable=False)
    title_ru: Mapped[str] = mapped_column(String(100), nullable=False)

    description_en: Mapped[str] = mapped_column(Text, nullable=False)
    description_kg: Mapped[str] = mapped_column(Text, nullable=False)
    description_ru: Mapped[str] = mapped_column(Text, nullable=False)

    image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )


class Contact(Base, IntIdMixin):
    branches: Mapped[str] = mapped_column(Text, nullable=True)
    funding_points: Mapped[str] = mapped_column(Text, nullable=True)
    phone_number: Mapped[str] = mapped_column(String(15), nullable=False)


class Product(Base, IntIdMixin):
    title_en: Mapped[str] = mapped_column(String(100), nullable=False)
    title_kg: Mapped[str] = mapped_column(String(100), nullable=False)
    title_ru: Mapped[str] = mapped_column(String(100), nullable=False)

    description_en: Mapped[str] = mapped_column(Text, nullable=False)
    description_kg: Mapped[str] = mapped_column(Text, nullable=False)
    description_ru: Mapped[str] = mapped_column(Text, nullable=False)

    image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )


class Partner(Base, IntIdMixin):
    title_en: Mapped[str] = mapped_column(String(100), nullable=False)
    title_kg: Mapped[str] = mapped_column(String(100), nullable=False)
    title_ru: Mapped[str] = mapped_column(String(100), nullable=False)

    description_en: Mapped[str] = mapped_column(Text, nullable=False)
    description_kg: Mapped[str] = mapped_column(Text, nullable=False)
    description_ru: Mapped[str] = mapped_column(Text, nullable=False)

    image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    video_url: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )


class ShariaCouncil(Base, IntIdMixin):
    fullname: Mapped[str] = mapped_column(String(100), nullable=False)

    description_en: Mapped[str] = mapped_column(Text, nullable=False)
    description_kg: Mapped[str] = mapped_column(Text, nullable=False)
    description_ru: Mapped[str] = mapped_column(Text, nullable=False)

    image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )


class News(Base, IntIdMixin):
    title_en: Mapped[str] = mapped_column(String(100), nullable=False)
    title_kg: Mapped[str] = mapped_column(String(100), nullable=False)
    title_ru: Mapped[str] = mapped_column(String(100), nullable=False)

    text_en: Mapped[str] = mapped_column(Text, nullable=False)
    text_kg: Mapped[str] = mapped_column(Text, nullable=False)
    text_ru: Mapped[str] = mapped_column(Text, nullable=False)

    image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    video_url: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )


class AboutUs(Base, IntIdMixin):
    title_en: Mapped[str] = mapped_column(String(100), nullable=False)
    title_kg: Mapped[str] = mapped_column(String(100), nullable=False)
    title_ru: Mapped[str] = mapped_column(String(100), nullable=False)

    description_en: Mapped[str] = mapped_column(Text, nullable=False)
    description_kg: Mapped[str] = mapped_column(Text, nullable=False)
    description_ru: Mapped[str] = mapped_column(Text, nullable=False)

    image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    video_url: Mapped[str] = mapped_column(String(255), nullable=True)


class CenterBanner(Base, IntIdMixin):
    title_en: Mapped[str] = mapped_column(String(100), nullable=False)
    title_kg: Mapped[str] = mapped_column(String(100), nullable=False)
    title_ru: Mapped[str] = mapped_column(String(100), nullable=False)

    description_en: Mapped[str] = mapped_column(Text, nullable=True)
    description_kg: Mapped[str] = mapped_column(Text, nullable=True)
    description_ru: Mapped[str] = mapped_column(Text, nullable=True)

    image_url: Mapped[str] = mapped_column(String(255), nullable=True)


class FinancialReport(Base, IntIdMixin):
    title_en: Mapped[str] = mapped_column(String, nullable=False)
    title_kg: Mapped[str] = mapped_column(String, nullable=False)
    title_ru: Mapped[str] = mapped_column(String, nullable=False)

    description_en: Mapped[str] = mapped_column(String, nullable=True)
    description_kg: Mapped[str] = mapped_column(String, nullable=True)
    description_ru: Mapped[str] = mapped_column(String, nullable=True)

    file_url: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )


class ProfitNorm(Base, IntIdMixin):
    title_en: Mapped[str] = mapped_column(String, nullable=False)
    title_kg: Mapped[str] = mapped_column(String, nullable=False)
    title_ru: Mapped[str] = mapped_column(String, nullable=False)

    description_en: Mapped[str] = mapped_column(String, nullable=True)
    description_kg: Mapped[str] = mapped_column(String, nullable=True)
    description_ru: Mapped[str] = mapped_column(String, nullable=True)

    file_url: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )
