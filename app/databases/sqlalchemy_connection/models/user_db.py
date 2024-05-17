from datetime import date, datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import Date, DateTime, ForeignKey, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import Base


class SpecializationArea(Base):
    __tablename__ = "specialization_areas"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255))


class UserDB(Base):
    __tablename__ = "users"

    uuid: Mapped[UUID] = mapped_column(Uuid(), primary_key=True, index=True, default=uuid4)
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    birth_date: Mapped[date] = mapped_column(Date())
    email: Mapped[str] = mapped_column(String(255), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    specialization_area_id: Mapped[int] = mapped_column(ForeignKey("specialization_areas.id"))
    specialization_area: Mapped[Optional["SpecializationArea"]] = relationship()
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), insert_default=func.CURRENT_TIMESTAMP())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), insert_default=func.CURRENT_TIMESTAMP())

    def __repr__(self):
        return f"<User(uuid={self.uuid},\n\
                   \tfirst_name={self.first_name},\n\
                   \tlast_name={self.last_name},\n\
                   \tbirth_date={self.birth_date},\n\
                   \temail={self.email},\n\
                   \tspecialization_area_id={self.specialization_area_id})>"
