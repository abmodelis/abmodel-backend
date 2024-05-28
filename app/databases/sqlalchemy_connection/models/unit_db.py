from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.databases.sqlalchemy_connection.base import Base


class UnitDB(Base):
    __tablename__ = "units"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String(255))
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    course: Mapped[Optional["CourseDB"]] = relationship(back_populates="units", lazy="noload")
    contents: Mapped[Optional[list["ContentDb"]]] = relationship(
        back_populates="unit",
    )

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), insert_default=func.CURRENT_TIMESTAMP())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), insert_default=func.CURRENT_TIMESTAMP())

    def __repr__(self):
        return f"<Unit(id={self.id},\n\
                   \ttitle={self.title},\n\
                   \tcourse_id={self.course_id},\n\
                   \tcreated_at={self.created_at},\n\
                   \tupdated_at={self.updated_at})>"


from .content_db import ContentDb
from .course_db import CourseDB
