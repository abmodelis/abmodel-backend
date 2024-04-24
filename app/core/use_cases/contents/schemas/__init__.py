from pydantic import BaseModel, Field


class ContentIn(BaseModel):
    title: str = Field(min_length=1, max_length=255, description="Titulo del contenido", examples=["Que es Python"])
    html_text: str = Field(
        min_length=1, max_length=255, description="Contenido del contenido", examples=["<h1>Python</h1>"]
    )
    media_path: str = Field(
        min_length=1, max_length=255, description="Ruta de la imagen del contenido", examples=["images/python.png"]
    )
    unit_id: int = Field(description="Id de la unidad", examples=[1])
