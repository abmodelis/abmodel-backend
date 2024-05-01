from datetime import datetime

from pydantic import BaseModel


class Unit(BaseModel):
    id: int
    title: str
    course_id: int
    # content: Optional[list["Content"]]
    created_at: datetime
    updated_at: datetime


