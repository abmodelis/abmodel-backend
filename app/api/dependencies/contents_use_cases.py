from fastapi import Depends

from app.core.use_cases.contents.crud import ContentCrud
from app.databases.sqlalchemy_connection.models.content_db import ContentDb

from .sqlalchemy_repo_dep import SQLARepoDeps


class SQLContentsCrud(ContentCrud):
    def __init__(self, repository=Depends(SQLARepoDeps(ContentDb))):
        super().__init__(repository)
