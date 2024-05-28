from datetime import UTC, datetime
from typing import Optional, TypeVar, Union
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.orm.decl_api import DeclarativeAttributeIntercept

from app.core.domain import Repository

EntityIn = TypeVar("EntityIn", bound=BaseModel)
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

    def update(self, entity: Union[EntityDB, int, UUID], entity_data: Optional[EntityIn] = None) -> Optional[EntityDB]:
        if isinstance(entity, (int, UUID)):
            entity_db = self.get_by_id(entity)
        elif isinstance(entity, self.Model):
            entity_db = entity
        else:
            return None

        if entity_db is None:
            return None

        if entity_data:
            if hasattr(entity_data, "restore") and getattr(entity_data, "restore", False):
                setattr(entity_db, "deleted_at", None)
            for key, value in entity_data.model_dump().items():
                setattr(entity_db, key, value)

        self.session.merge(entity_db)
        self.session.commit()
        self.session.refresh(entity_db)
        return entity_db

    def get_by(self, *args, **kwargs) -> Optional[EntityDB]:
        return self.session.query(self.Model).filter_by(*args, **kwargs).first()

    def get_by_id(self, entity_id: int | UUID) -> Optional[EntityDB]:
        return self.session.query(self.Model).get(entity_id)

    def get_all(self, query_params: Optional[BaseModel] = None) -> list[EntityDB]:
        query = self.session.query(self.Model)

        if not query_params:
            return query.all()

        query = query.filter_by(**query_params.model_dump(exclude_none=True))
        archived = getattr(query_params, "archived", False)

        if not hasattr(self.Model, "deleted_at"):
            return query.all()

        if archived:
            query = query.filter(self.Model.deleted_at.isnot(None))  # type: ignore
            return query.all()

        query = query.filter_by(deleted_at=None)
        return query.all()

    def delete(self, entity: EntityDB | int | UUID) -> Optional[EntityDB]:
        if isinstance(entity, (int, UUID)):
            entity_db = self.get_by_id(entity)
        elif isinstance(entity, self.Model):
            entity_db = entity
        else:
            return None

        self.session.delete(entity_db)
        self.session.commit()
        return entity_db

    def soft_delete(self, entity: EntityDB | int | UUID) -> Optional[EntityDB]:
        if isinstance(entity, (int, UUID)):
            entity_db = self.get_by_id(entity)
        elif isinstance(entity, self.Model):
            entity_db = entity
        else:
            return None

        entity_db.deleted_at = datetime.now(UTC)  # type: ignore
        self.session.merge(entity_db)
        self.session.commit()
        self.session.refresh(entity_db)
        return entity_db
