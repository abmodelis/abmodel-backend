from fastapi import APIRouter
from .course_routes import router as course_router


api_route = APIRouter(prefix="/api/v1")
api_route.include_router(course_router, prefix="/courses", tags=["courses"])
