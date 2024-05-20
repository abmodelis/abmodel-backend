from datetime import datetime

from pydantic import BaseModel


class Content(BaseModel):
    id: int
    title: str
    html_text: str
    media_path: str
    created_at: datetime
    updated_at: datetime
