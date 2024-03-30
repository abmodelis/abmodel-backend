from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict


class Status(Enum):
    NO_VISIBLE = 0
    VISIBLE = 1

    def __int__(self):
        return self.value


class Course(BaseModel):
    id: int
    title: str
    description: str
    status: Status
    price: int
    image_path: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]
    # owner: Optional[User]

    model_config = ConfigDict(from_attributes=True)
