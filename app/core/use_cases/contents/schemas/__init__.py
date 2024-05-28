from pydantic import BaseModel, Field


class ContentIn(BaseModel):
    title: str = Field(min_length=1, max_length=255, description="Titulo de la clase/contenido", examples=["Introducción"])
    html_text: str = Field(min_length=0, description="Contenido del contenido", examples=["# Python"])
    media_path: str = Field(min_length=0, description="Ruta de la imagen del contenido", examples=["images/python.png"])
    unit_id: int = Field(description="Id de la unidad", examples=[1])
