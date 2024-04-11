from app.core.domain.repository import Repository
from app.databases.sqlalchemy_connection.models.course_db import CourseDB

from .schemas import CourseIn


class CoursesCrud:
    def __init__(self, repository: Repository[CourseIn, CourseDB]) -> None:
        self.repository = repository

    def create(self, course_in: CourseIn):
        return self.repository.create(course_in)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, entity_id: int):
        course = self.repository.get_by_id(entity_id)
        return course

    def update(self, entity_id: int, course_in: CourseIn):
        course = self.get_by_id(entity_id)
        if not course:
            return None
        for key, value in course_in.model_dump().items():
            setattr(course, key, value)
        return self.repository.update(course)

    def soft_delete(self, entity_id: int):
        course = self.get_by_id(entity_id)
        if not course:
            return None
        return self.repository.soft_delete(course)
