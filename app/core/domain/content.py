from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from .unit import Unit


class Content(BaseModel):
    id: int
    title: str
    html_text: str
    media_path: str
    created_at: datetime
    updated_at: datetime
    unit: Optional[Unit]
