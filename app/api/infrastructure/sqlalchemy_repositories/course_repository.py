from fastapi import Depends
from pydantic import TypeAdapter
from sqlalchemy.orm import Session

from app.api.dependencies.get_db import get_db
from app.core.domain import Repository
from app.core.domain.course import Course
from app.core.use_cases.courses.schemas import CourseIn
from app.databases.sqlalchemy_connection.models.course_db import CourseDB


class CourseRepository(Repository[CourseIn, Course]):
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def create(self, entity):
        new_course = CourseDB(**entity.model_dump())
        self.db.add(new_course)
        self.db.commit()
        self.db.refresh(new_course)
        return TypeAdapter(Course).validate_python(new_course)

    def get_all(self):
        courses = self.db.query(CourseDB).all()
        return TypeAdapter(list[Course]).validate_python(courses)

    def get_by_id(self, entity_id):
        raise NotImplementedError

    def delete(self, entity_id):
        raise NotImplementedError

    def update(self, entity):
        raise NotImplementedError

    def update_by_id(self, entity_id, entity):
        raise NotImplementedError
