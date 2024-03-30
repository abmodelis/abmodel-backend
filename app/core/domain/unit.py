from dataclasses import dataclass
from typing import Optional

from .course import Course


@dataclass
class Unit:
    id: int
    title: str
    description: str
    course: Optional[Course]
