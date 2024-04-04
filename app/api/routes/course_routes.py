from fastapi import APIRouter, Depends

from app.core.domain.course import Course
from app.core.use_cases.courses.schemas import CourseIn

from ..dependencies.course_use_cases import SQLCoursesCrud
from ..dependencies.jwt import CurrenUserDependency

router = APIRouter()


@router.post("/", dependencies=[CurrenUserDependency])
def create_course(course_in: CourseIn, crud: SQLCoursesCrud = Depends()) -> Course:
    course_in.price = int(course_in.price * 100)  # Convert to cents
    return crud.create(course_in)


@router.get("/", dependencies=[CurrenUserDependency])
def get_all_courses(crud: SQLCoursesCrud = Depends()) -> list[Course]:
    return crud.get_all()
