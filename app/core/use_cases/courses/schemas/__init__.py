from pydantic import BaseModel, Field

from app.core.domain import Status


class CourseIn(BaseModel):
    title: str = Field(min_length=1, max_length=255, description="Titulo del curso", examples=["Python", "FastAPI"])
    description: str = Field(description="Descripcion del curso", examples=["Curso de Python", "Curso de FastAPI"])
    price: int = Field(ge=0, description="Precio ej: 100.00 bs", examples=[100])
    status: Status = Field(
        default=Status.NO_VISIBLE, description="Estado del curso, 0-No visible, 1-Visible", examples=[0, 1]
    )
    image_path: str = Field(
        min_length=1, max_length=255, description="Ruta de la imagen del curso", examples=["images/python.png"]
    )
