from app.core.domain import Content, Repository
from app.core.use_cases.contents.schemas import ContentIn


class ContentCrud:
    def __init__(self, repository: Repository[ContentIn, Content]) -> None:
        self.repository = repository

    def create(self, content_in: ContentIn):
        return self.repository.create(content_in)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, entity_id: int):
        return self.repository.get_by_id(entity_id)

    def update(self, entity_id: int, content_in: ContentIn):
        return self.repository.update(entity_id, content_in)

    def delete(self, entity_id: int):
        return self.repository.delete(entity_id)
