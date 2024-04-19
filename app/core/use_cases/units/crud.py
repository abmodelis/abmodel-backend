from app.core.domain import Unit
from app.core.domain.repository import Repository
from app.core.use_cases.units.schemas import UnitIn


class UnitCrud:
    def __init__(self, repository: Repository[UnitIn, Unit]) -> None:
        self.repository = repository

    def create(self, unit_in: UnitIn):
        return self.repository.create(unit_in)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, entity_id: int):
        return self.repository.get_by_id(entity_id)

    def update(self, entity_id: int, unit_in: UnitIn):
        return self.repository.update(entity_id, unit_in)

    def delete(self, entity_id: int):
        return self.repository.delete(entity_id)
