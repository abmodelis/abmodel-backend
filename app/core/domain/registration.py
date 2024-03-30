from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .course import Course
from .user import User


@dataclass
class Registration:
    id: int
    user: Optional[User]
    course: Optional[Course]
    rate: int
    comment: str
    created_at: datetime
    updated_at: datetime
