from fastapi import APIRouter
from .course_routes import router as course_router
from .multimedia_routes import router as multimedia_router
from .authorizations import router as authorization_router


api_route = APIRouter(prefix="/api/v1")
api_route.include_router(authorization_router, prefix="/auth", tags=["auth"])
api_route.include_router(course_router, prefix="/courses", tags=["courses"])
api_route.include_router(multimedia_router, prefix="/multimedia", tags=["multimedia"])
