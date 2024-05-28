from fastapi import Depends

from app.core.use_cases.specializations import GetAll
from app.databases.sqlalchemy_connection.models.user_db import \
    SpecializationArea

from ..sqlalchemy_repo_dep import SQLARepoDeps


class ApiGetAll(GetAll):
    def __init__(self, repository=Depends(SQLARepoDeps(SpecializationArea))) -> None:
        super().__init__(repository)
