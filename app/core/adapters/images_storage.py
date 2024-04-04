from abc import ABC, abstractmethod


class ImagesStorage(ABC):

    @abstractmethod
    def upload(self, file): ...
