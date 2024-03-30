from pydantic import BaseModel

from app.core.domain import Status


class CourseIn(BaseModel):
    title: str
    description: str
    price: int
    status: Status
    image_path: str
