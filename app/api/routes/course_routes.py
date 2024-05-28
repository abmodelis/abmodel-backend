from fastapi import APIRouter, Depends, HTTPException

from app.core.domain.course import Course
from app.core.use_cases.courses.schemas import CourseIn, CourseQueryParams

from ..dependencies.course_use_cases import SQLCoursesCrud
from ..dependencies.jwt import CurrenUserDependency

router = APIRouter()


@router.post("/", dependencies=[CurrenUserDependency], response_model=Course)
async def create_course(course_in: CourseIn, crud: SQLCoursesCrud = Depends()):
    return crud.create(course_in)


@router.get("/", dependencies=[CurrenUserDependency], response_model=list[Course])
async def get_all_courses(query_params: CourseQueryParams = Depends(), crud: SQLCoursesCrud = Depends()):
    return crud.get_all(query_params)


@router.get("/{entity_id}", dependencies=[CurrenUserDependency], response_model=Course)
async def get_by_id(entity_id: int, crud: SQLCoursesCrud = Depends()):
    course = crud.get_by_id(entity_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.put("/{entity_id}", dependencies=[CurrenUserDependency], response_model=Course)
async def update_by_id(entity_id: int, course_in: CourseIn, crud: SQLCoursesCrud = Depends()):
    course = crud.update(entity_id, course_in)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.delete("/{entity_id}", dependencies=[CurrenUserDependency], response_model=Course)
async def delete_by_id(entity_id: int, crud: SQLCoursesCrud = Depends()):
    course = crud.soft_delete(entity_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
