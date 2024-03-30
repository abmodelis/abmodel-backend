from fastapi import APIRouter, Depends

from app.core.domain.course import Course
from app.core.use_cases.courses.schemas import CourseIn

from ..dependencies.course_use_cases import SQLCoursesCrud

router = APIRouter()


@router.post("/")
def create_course(course_in: CourseIn, crud: SQLCoursesCrud = Depends()) -> Course:
    return crud.create(course_in)


@router.get("/")
def get_all_courses(crud: SQLCoursesCrud = Depends()) -> list[Course]:
    return crud.get_all()
