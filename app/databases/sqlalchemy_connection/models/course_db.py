from datetime import UTC, datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.core.domain.course import Status
from app.databases.sqlalchemy_connection.base import Base


class CourseDB(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    status = Column(Integer, default=Status.NO_VISIBLE)
    price = Column(Integer)
    image_path = Column(String(255))
    created_at = Column(DateTime, default=datetime.now(UTC), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(UTC), nullable=False, onupdate=datetime.now(UTC))
    deleted_at = Column(DateTime, default=None, nullable=True)

    # owner: Column[]
