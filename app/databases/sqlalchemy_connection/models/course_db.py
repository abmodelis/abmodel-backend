from datetime import UTC, datetime

from sqlalchemy import Column, DateTime, Enum, Integer, String, Text

from app.core.domain.course import Status
from app.databases.sqlalchemy_connection.base import Base


class CourseDB(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    status = Column(Enum(Status), default=Status.NO_VISIBLE)
    price = Column(Integer)
    image_path = Column(String(255))
    created_at = Column(DateTime, default=datetime.now(UTC), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(UTC), nullable=False, onupdate=datetime.now(UTC))
    deleted_at = Column(DateTime, default=None, nullable=True)

    # owner: Column[]

    def __repr__(self):
        return f"<Course(id={self.id}, title={self.title}, description={self.description}, status={self.status}, price={self.price}, image_path={self.image_path}, created_at={self.created_at}, updated_at={self.updated_at}, deleted_at={self.deleted_at})>"
