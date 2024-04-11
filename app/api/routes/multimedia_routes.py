from http.client import BAD_REQUEST

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from pydantic import BaseModel, Field

from app.api.dependencies.upload_image_use_case import CloudUploadImage

from ..dependencies.jwt import CurrenUserDependency

router = APIRouter()


class ImagesUrl(BaseModel):
    image_url: str = Field(
        min_length=1,
        max_length=255,
        description="Url de la imagen",
        examples=["http://res.cloudinary.com/dv7lb2949/image/upload/v1712162130/gr2tddmzefbemyrxwd7c.jpg"],
    )


@router.post("/images", dependencies=[CurrenUserDependency])
def upload_images(file: UploadFile = File(...), upload_image: CloudUploadImage = Depends()) -> ImagesUrl:
    if not file:
        raise HTTPException(status_code=BAD_REQUEST, detail="No file")
    if not (file.content_type or "").startswith("image"):
        raise HTTPException(status_code=BAD_REQUEST, detail="Not an image")
    url = upload_image(file.file)
    return ImagesUrl(image_url=url)
