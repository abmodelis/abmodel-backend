from app.core.domain import Unit
from app.core.domain.repository import Repository

from .schemas import UnitIn, UnitQueryParams


class UnitCrud:
    def __init__(self, repository: Repository[UnitIn, Unit]) -> None:
        self.repository = repository

    def create(self, unit_in: UnitIn):
        return self.repository.create(unit_in)

    def get_all(self, query: UnitQueryParams):
        return self.repository.get_all(query)

    def get_by_id(self, entity_id: int):
        return self.repository.get_by_id(entity_id)

    def update(self, entity_id: int, unit_in: UnitIn):
        unit = self.get_by_id(entity_id)
        if not unit:
            return None
        for key, value in unit_in.model_dump().items():
            setattr(unit, key, value)
        return self.repository.save(unit)

    def delete(self, entity_id: int):
        units = self.get_by_id(entity_id)
        if not units:
            return None
        return self.repository.delete(units)
