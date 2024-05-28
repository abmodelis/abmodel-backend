from abc import ABC, abstractmethod
from typing import BinaryIO


class ImagesStorage(ABC):

    @abstractmethod
    def upload(self, file: BinaryIO) -> str: ...
