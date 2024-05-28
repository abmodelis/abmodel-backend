from fastapi import APIRouter

from .authorizations import router as authorization_router
from .content_routes import router as content_router
from .course_routes import router as course_router
from .multimedia_routes import router as multimedia_router
from .unit_routes import router as unit_router
from .user_routes import router as user_router

api_route = APIRouter(prefix="/api/v1")
api_route.include_router(authorization_router, prefix="/auth", tags=["auth"])
api_route.include_router(course_router, prefix="/courses", tags=["courses"])
api_route.include_router(multimedia_router, prefix="/multimedia", tags=["multimedia"])
api_route.include_router(unit_router, prefix="/units", tags=["units"])
api_route.include_router(content_router, prefix="/contents", tags=["Contents"])
api_route.include_router(user_router, prefix="/users", tags=["users"])
