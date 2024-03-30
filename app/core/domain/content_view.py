from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .content import Content
from .registration import Registration


@dataclass
class ContentView:
    id: int
    registration: Optional[Registration]
    content: Optional[Content]
    created_at: datetime
    updated_at: datetime
