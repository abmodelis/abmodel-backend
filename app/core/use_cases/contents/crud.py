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
        content = self.get_by_id(entity_id)
        if not content:
            return None
        for key, value in content_in.model_dump().items():
            setattr(content, key, value)
        return self.repository.save(content)

    def delete(self, entity_id: int):
        content = self.get_by_id(entity_id)
        if not content:
            return None
        return self.repository.delete(content)
