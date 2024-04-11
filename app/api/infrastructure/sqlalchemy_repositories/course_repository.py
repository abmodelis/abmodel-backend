from datetime import UTC, datetime

from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.dependencies.get_db import get_db
from app.core.domain import Repository
from app.core.use_cases.courses.schemas import CourseIn
from app.databases.sqlalchemy_connection.models.course_db import CourseDB


class CourseRepository(Repository[CourseIn, CourseDB]):
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def create(self, entity):
        new_course = CourseDB(**entity.model_dump())
        self.db.add(new_course)
        self.db.commit()
        self.db.refresh(new_course)
        return new_course

    def get_all(self):
        return self.db.query(CourseDB).all()

    def get_by_id(self, entity_id):
        course = self.db.query(CourseDB).filter_by(id=entity_id, deleted_at=None).first()
        return course

    def update(self, entity: CourseDB):
        self.db.merge(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def soft_delete(self, entity: CourseDB):
        entity.deleted_at = datetime.now(UTC)
        self.db.merge(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity
