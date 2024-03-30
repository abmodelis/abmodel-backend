from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from .content import Content
from .registration import Registration


class ContentView(BaseModel):
    id: int
    registration: Optional[Registration]
    content: Optional[Content]
    created_at: datetime
    updated_at: datetime
