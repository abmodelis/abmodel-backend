import os
from typing import BinaryIO

import cloudinary
from cloudinary.uploader import upload

from app.core.adapters.images_storage import ImagesStorage


class CloudinaryAdapter(ImagesStorage):

    def __init__(self):
        cloudinary.config(
            cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME", ""),
            api_key=os.getenv("CLOUDINARY_API_KEY", ""),
            api_secret=os.getenv("CLOUDINARY_API_SECRET", ""),
        )

    def upload(self, file: BinaryIO) -> str:
        response = upload(file)
        return response.get("url")
