from dataclasses import dataclass
from enum import Enum
from uuid import UUID


class Role(Enum):
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"


@dataclass
class User:
    uuid: UUID
    first_name: str
    last_name: str
    email: str
    role: Role
