from pydantic import BaseModel, Field


class ContentIn(BaseModel):
    html_text: str = Field(min_length=0, description="Contenido del contenido", examples=["# Python"])
    media_path: str = Field(min_length=0, description="Ruta de la imagen del contenido", examples=["images/python.png"])
    unit_id: int = Field(description="Id de la unidad", examples=[1])
