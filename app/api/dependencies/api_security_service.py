from fastapi import Depends

from app.core.use_cases.auth import SecurityService
from app.databases.sqlalchemy_connection.models import UserDB
from app.env import Env

from .sqlalchemy_repo_dep import SQLARepoDeps


class ApiSecurityService(SecurityService):
    def __init__(
        self,
        repository=Depends(SQLARepoDeps(UserDB)),
        secret: str = Depends(lambda: Env.SECRET_KEY),
        algorithm: str = Depends(lambda: Env.ALGORITHM),
    ) -> None:
        super().__init__(repository, secret, algorithm)
