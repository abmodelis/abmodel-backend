from app.core.domain import Repository, SpecializationArea


class GetAll:
    def __init__(self, repository: Repository[None, SpecializationArea]) -> None:
        self.repository = repository

    def __call__(self) -> list[SpecializationArea]:
        return self.repository.get_all()
