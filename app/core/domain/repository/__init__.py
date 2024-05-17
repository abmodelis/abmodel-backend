# mypy: ignore-errors
from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, overload
from uuid import UUID

from pydantic import BaseModel

EntityIn = TypeVar("EntityIn")
EntityDB = TypeVar("EntityDB")


class Repository(ABC, Generic[EntityIn, EntityDB]):

    @abstractmethod
    def get_all(self, query_params: Optional[BaseModel] = None) -> list[EntityDB]: ...

    @abstractmethod
    def create(self, entity: EntityIn) -> EntityDB: ...

    @abstractmethod
    def save(self, entity: EntityDB) -> EntityDB: ...

    @overload
    @abstractmethod
    def get_by_id(self, entity_id: int) -> Optional[EntityDB]: ...

    @overload
    @abstractmethod
    def get_by_id(self, entity_id: UUID) -> Optional[EntityDB]: ...

    @overload
    @abstractmethod
    def delete(self, entity: EntityDB) -> Optional[EntityDB]: ...

    @overload
    @abstractmethod
    def delete(self, entity_id: int | UUID) -> Optional[EntityDB]: ...

    @overload
    @abstractmethod
    def soft_delete(self, entity: EntityDB) -> Optional[EntityDB]: ...

    @overload
    @abstractmethod
    def soft_delete(self, entity_id: int | UUID) -> Optional[EntityDB]: ...

    @overload
    @abstractmethod
    def update(self, entity: EntityDB) -> Optional[EntityDB]: ...

    @overload
    @abstractmethod
    def update(self, entity_id: int | UUID, entity_in: EntityIn) -> Optional[EntityDB]: ...

    @abstractmethod
    def get_by(self, *args, **kwargs) -> Optional[EntityDB]: ...
