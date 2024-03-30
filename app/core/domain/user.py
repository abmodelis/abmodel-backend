from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class Role(Enum):
    ADMIN = 0
    TEACHER = 1
    STUDENT = 2


class User(BaseModel):
    uuid: UUID
    first_name: str
    last_name: str
    email: str
    role: Role
