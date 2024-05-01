from typing import Optional

from pydantic import BaseModel, Field


class UnitIn(BaseModel):
    title: str = Field(min_length=1, max_length=255, description="Titulo de la unidad", examples=["Introducción"])
    course_id: int = Field(description="Id del curso al que pertenece la unidad", examples=[1])


class UnitQueryParams(BaseModel):
    course_id: Optional[int] = Field(None, description="Id del curso al que pertenece la unidad", examples=[1])
