from typing import Optional

from pydantic import BaseModel

from .course import Course


class Unit(BaseModel):
    id: int
    title: str
    description: str
    course: Optional[Course]
