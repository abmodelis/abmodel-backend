from typing import BinaryIO

import cloudinary
from cloudinary.uploader import upload

from app.core.adapters.images_storage import ImagesStorage
from app.env import Env


class CloudinaryAdapter(ImagesStorage):

    def __init__(self):
        cloudinary.config(
            cloud_name=Env.CLOUDINARY_CLOUD_NAME,
            api_key=Env.CLOUDINARY_API_KEY,
            api_secret=Env.CLOUDINARY_API_SECRET,
        )

    def upload(self, file: BinaryIO) -> str:
        response = upload(file)
        return response.get("url")
