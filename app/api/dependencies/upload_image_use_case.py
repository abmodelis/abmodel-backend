from typing import BinaryIO
from fastapi import Depends, HTTPException, status
from app.api.infrastructure.cloudinary_adapter import CloudinaryAdapter
from app.core.use_cases.courses.upload_image import UploadImages


class CloudUploadImage(UploadImages):
    def __init__(self, image_storage: CloudinaryAdapter = Depends()) -> None:
        super().__init__(image_storage)

    def __call__(self, file: BinaryIO):
        try:
            return self.image_storage.upload(file)
        except Exception as error:
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(error)) from error
