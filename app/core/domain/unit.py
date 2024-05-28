from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Unit(BaseModel):
    id: int
    title: str
    course_id: int
    contents: Optional[list["Content"]]
    created_at: datetime
    updated_at: datetime


from .content import Content
