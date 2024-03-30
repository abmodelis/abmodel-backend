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
