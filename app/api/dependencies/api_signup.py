from fastapi import Depends

from app.core.use_cases.auth import SignUp
from app.databases.sqlalchemy_connection.models.user_db import UserDB

from .sqlalchemy_repo_dep import SQLARepoDeps


class APISignUp(SignUp):
    def __init__(self, repository=Depends(SQLARepoDeps(UserDB))) -> None:
        super().__init__(repository)
