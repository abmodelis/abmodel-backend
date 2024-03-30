from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class Status(Enum):
    NO_VISIBLE = 0
    VISIBLE = 1


@dataclass
class Course:
    id: int
    title: str
    description: str
    status: Status
    price: int
    image_path: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    # owner: Optional[User]
