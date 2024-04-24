from fastapi import Depends

from app.core.use_cases.courses.crud import CoursesCrud
from app.databases.sqlalchemy_connection.models.course_db import CourseDB

from .sqlalchemy_repo_dep import SQLARepoDeps


class SQLCoursesCrud(CoursesCrud):
    def __init__(self, repository=Depends(SQLARepoDeps(CourseDB))):
        super().__init__(repository)
