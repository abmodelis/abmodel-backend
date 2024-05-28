from typing import Optional
from pydantic import BaseModel, Field

from app.core.domain import Status


class CourseIn(BaseModel):
    title: str = Field(min_length=1, max_length=255, description="Titulo del curso", examples=["Python", "FastAPI"])
    description: str = Field(description="Descripcion del curso", examples=["Curso de Python", "Curso de FastAPI"])
    price: int = Field(ge=0, description="Precio en centavos ej: 100.00 bs => 10000", examples=[10000])
    status: Status = Field(
        default=Status.NO_VISIBLE,
        description="Estado del curso, 0-No visible, 1-Visible",
        examples=[0, 1],
    )
    image_path: str = Field(
        min_length=1,
        max_length=255,
        description="Ruta de la imagen del curso",
        examples=["images/python.png"],
    )
    restore: Optional[bool] = Field(
        None,
        description="Restaurar curso archivado",
        examples=[0, 1, "true", "false"],
        exclude=True,
    )


class CourseQueryParams(BaseModel):
    archived: Optional[bool] = Field(
        None,
        description="Obtener cursos Archivados",
        examples=[0, 1, "true", "false"],
        exclude=True,
    )
