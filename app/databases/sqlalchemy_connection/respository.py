from datetime import UTC, datetime
from typing import Optional, TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.orm.decl_api import DeclarativeAttributeIntercept

from app.core.domain import Repository

EntityIn = TypeVar("EntityIn")
EntityDB = TypeVar("EntityDB")


class SQLARepository(Repository[EntityIn, EntityDB]):

    def __init__(self, Model: DeclarativeAttributeIntercept, session: Session) -> None:
        self.Model = Model
        self.session = session

    def create(self, entity: BaseModel) -> EntityDB:
        model = self.Model(**entity.model_dump())
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model

    def save(self, entity: EntityDB) -> EntityDB:
        if entity.id:  # type: ignore
            self.session.merge(entity)
        else:
            self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def update(self, entity: EntityDB) -> Optional[EntityDB]:
        self.session.merge(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def get_by_id(self, entity_id: int) -> Optional[EntityDB]:
        return self.session.query(self.Model).get(entity_id)

    def get_all(self, query_params: Optional[BaseModel] = None) -> list[EntityDB]:
        query = self.session.query(self.Model)
        if query_params:
            query = query.filter_by(**query_params.model_dump(exclude_none=True))
        entities = query.all()
        return entities

    def delete(self, entity: EntityDB) -> Optional[EntityDB]:
        self.session.delete(entity)
        self.session.commit()
        return entity

    def soft_delete(self, entity: EntityDB) -> Optional[EntityDB]:
        entity.deleted_at = datetime.now(UTC)  # type: ignore
        self.session.merge(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity
