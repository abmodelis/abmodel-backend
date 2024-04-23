from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.orm.decl_api import DeclarativeAttributeIntercept

from app.databases.sqlalchemy_connection.respository import SQLARepository

from .get_db import get_db


class SQLARepoDeps(SQLARepository):

    # pylint: disable=super-init-not-called
    def __init__(self, Model: DeclarativeAttributeIntercept) -> None:
        self.Model = Model

    def __call__(self, session: Session = Depends(get_db)) -> "SQLARepoDeps":
        self.session = session
        return self
