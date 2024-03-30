from pydantic import BaseModel, Field

from app.core.domain import Status


class CourseIn(BaseModel):
    title: str = Field(min_length=1, max_length=255, description="Titulo del curso")
    description: str = Field(description="Descripcion del curso")
    price: int = Field(gt=0, description="Precio en centavos")
    status: Status = Field(default=Status.NO_VISIBLE, description="Estado del curso, 0-No visible, 1-Visible")
    image_path: str = Field(min_length=1, max_length=255, description="Ruta de la imagen del curso")
