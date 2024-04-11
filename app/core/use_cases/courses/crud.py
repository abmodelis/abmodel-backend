from app.core.domain import Course
from app.core.domain.repository import Repository

from .schemas import CourseIn


class CoursesCrud:
    def __init__(self, repository: Repository[CourseIn, Course]) -> None:
        self.repository = repository

    def create(self, course_in: CourseIn) -> Course:
        return self.repository.create(course_in)

    def get_all(self) -> list[Course]:
        return self.repository.get_all()

    def get_by_id(self, entity_id: int) -> Course | None:
        course = self.repository.get_by_id(entity_id)
        if course is None:
            return None
        course.price = int(course.price / 100) # convert to bolivianos
        return course
