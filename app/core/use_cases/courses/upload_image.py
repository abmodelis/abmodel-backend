from typing import BinaryIO

from app.core.adapters.images_storage import ImagesStorage


class UploadImages:
    def __init__(self, images_storage: ImagesStorage) -> None:
        self.image_storage = images_storage

    def __call__(self, file: BinaryIO) -> str:
        return self.image_storage.upload(file)
