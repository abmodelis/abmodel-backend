from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .unit import Unit


@dataclass
class Content:
    id: int
    title: str
    html_text: str
    media_path: str
    created_at: datetime
    updated_at: datetime
    unit: Optional[Unit]
