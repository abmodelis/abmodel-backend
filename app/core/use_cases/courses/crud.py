from typing import Optional
from app.core.domain.course import Course
from app.core.domain.repository import Repository

from .schemas import CourseIn, CourseQueryParams


class CoursesCrud:
    def __init__(self, repository: Repository[CourseIn, Course]) -> None:
        self.repository = repository

    def create(self, course_in: CourseIn):
        return self.repository.create(course_in)

    def get_all(self, query_params: Optional[CourseQueryParams] = None):
        return self.repository.get_all(query_params)

    def get_by_id(self, entity_id: int):
        course = self.repository.get_by_id(entity_id)
        return course

    def update(self, entity_id: int, course_in: CourseIn):
        course = self.get_by_id(entity_id)
        if not course:
            return None
        if course_in.restore:
            course.deleted_at = None
        for key, value in course_in.model_dump().items():
            setattr(course, key, value)
        return self.repository.update(course)

    def soft_delete(self, entity_id: int):
        course = self.get_by_id(entity_id)
        if not course:
            return None
        return self.repository.soft_delete(course)
