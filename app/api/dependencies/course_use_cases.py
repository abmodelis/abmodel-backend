from fastapi import Depends

from app.api.infrastructure.sqlalchemy_repositories import CourseRepository
from app.core.use_cases.courses.crud import CoursesCrud


class SQLCoursesCrud(CoursesCrud):
    def __init__(self, repository: CourseRepository = Depends()):
        super().__init__(repository)
