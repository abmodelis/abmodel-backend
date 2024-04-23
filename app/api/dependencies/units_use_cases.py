from fastapi import Depends

from app.core.use_cases.units.crud import UnitCrud
from app.databases.sqlalchemy_connection.models.unit_db import UnitDB

from .sqlalchemy_repo_dep import SQLARepoDeps


class SQLUnitCrud(UnitCrud):
    def __init__(self, repository=Depends(SQLARepoDeps(UnitDB))) -> None:
        super().__init__(repository)
