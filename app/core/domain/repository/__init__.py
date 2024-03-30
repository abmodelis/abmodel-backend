from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, overload
from uuid import UUID

EntityIn = TypeVar("EntityIn")
Entity = TypeVar("Entity")


class Repository(ABC, Generic[EntityIn, Entity]):

    @abstractmethod
    def get_all(self) -> list[Entity]: ...

    @abstractmethod
    def create(self, entity: EntityIn) -> Entity: ...

    @overload
    @abstractmethod
    def get_by_id(self, entity_id: int) -> Optional[Entity]: ...

    @overload
    @abstractmethod
    def get_by_id(self, entity_id: UUID) -> Optional[Entity]: ...

    @overload
    @abstractmethod
    def delete(self, entity_id: int) -> Optional[Entity]: ...

    @overload
    @abstractmethod
    def delete(self, entity_id: UUID) -> Optional[Entity]: ...

    @overload
    @abstractmethod
    def update(self, entity: EntityIn) -> Optional[Entity]: ...

    @overload
    @abstractmethod
    def update(self, entity_id: int, entity: EntityIn) -> Optional[Entity]: ...

    @overload
    @abstractmethod
    def update(self, entity_id: UUID, entity: EntityIn) -> Optional[Entity]: ...
