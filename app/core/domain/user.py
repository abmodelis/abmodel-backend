from datetime import date
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, SecretStr


class Role(Enum):
    ADMIN = 0
    TEACHER = 1
    STUDENT = 2


class SpecializationArea(BaseModel):
    id: int
    title: str


class User(BaseModel):
    uuid: UUID
    first_name: str
    last_name: str
    birth_date: date
    specialization_area: Optional[SpecializationArea]
    email: str
    role: Optional[Role] = Field(None)  # TODO: Remove Optional when roles will be implemented
    hashed_password: SecretStr = Field(exclude=True)
