from datetime import date
from typing import Optional

from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr, Field, SecretStr, computed_field


class UserLogin(BaseModel):
    email: EmailStr = Field(title="Email", min_length=1, max_length=255)
    password: SecretStr = Field(
        title="Contraseña",
        description="Contraseña del usuario",
        examples=["123456"],
        min_length=8,
        max_length=255,
        json_schema_extra={"writeOnly": True},
    )


class UserIn(BaseModel):
    first_name: str = Field(title="Nombres", min_length=1, max_length=255, examples=["John", "Jane"])
    last_name: str = Field(title="Apellidos", min_length=1, max_length=255, examples=["Doe", "Smith"])
    email: EmailStr = Field(title="Email", min_length=1, max_length=255, examples=["john.doe@email.com"])
    password: SecretStr = Field(
        exclude=True,
        title="Contraseña",
        description="Contraseña del usuario",
        examples=["ABC123456"],
        min_length=8,
        max_length=255,
        json_schema_extra={"writeOnly": True},
    )
    birth_date: date = Field(title="Fecha de nacimiento", examples=["1990-01-01"])
    specialization_area_id: Optional[int] = Field(None, title="Area de especialidad", ge=1, examples=[1])

    @computed_field
    @property
    def hashed_password(self) -> str:
        pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
        return pwd_context.hash(self.password.get_secret_value())  # pylint: disable=no-member
