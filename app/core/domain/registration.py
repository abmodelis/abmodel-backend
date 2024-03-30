from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from .course import Course
from .user import User


class Registration(BaseModel):
    id: int
    user: Optional[User]
    course: Optional[Course]
    rate: int
    comment: str
    created_at: datetime
    updated_at: datetime
