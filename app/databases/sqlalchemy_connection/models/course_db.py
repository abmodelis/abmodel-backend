from datetime import datetime

from sqlalchemy import DateTime, Enum, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.domain.course import Status
from app.databases.sqlalchemy_connection.base import Base


class CourseDB(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(Enum(Status), default=Status.NO_VISIBLE)
    price: Mapped[int] = mapped_column(Integer)
    image_path: Mapped[str] = mapped_column(String(255))
    units: Mapped[list["UnitDB"]] = relationship(back_populates="courses")

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), insert_default=func.CURRENT_TIMESTAMP())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), insert_default=func.CURRENT_TIMESTAMP())
    deleted_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    # owner: Column[]

    def __repr__(self):
        return f"<Course(id={self.id},\n\
                       \ttitle={self.title},\n\
                       \tdescription={self.description},\n\
                       \tstatus={self.status},\n\
                       \tprice={self.price},\n\
                       \timage_path={self.image_path},\n\
                       \tcreated_at={self.created_at},\n\
                       \tupdated_at={self.updated_at},\n\
                       \tdeleted_at={self.deleted_at})>"


from .unit_db import UnitDB
