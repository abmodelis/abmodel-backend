from fastapi import Depends

from app.core.use_cases.auth import SignIn
from app.databases.sqlalchemy_connection.models import UserDB

from .sqlalchemy_repo_dep import SQLARepoDeps


class APISignIn(SignIn):
    def __init__(self, repository=Depends(SQLARepoDeps(UserDB))) -> None:
        super().__init__(repository)
