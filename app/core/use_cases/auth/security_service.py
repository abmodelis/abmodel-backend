from datetime import UTC, datetime, timedelta
from typing import MutableMapping, Optional
from uuid import UUID

from jose import jwt

from app.core.domain import Repository, TokenDict, User

from .schemas import UserIn


class SecurityService:
    def __init__(self, repository: Repository[UserIn, User], secret: str, algorithm: str) -> None:
        self.repository = repository
        self.__secret = secret
        self.__algorithm = algorithm

    def __create_token(self, to_encode: MutableMapping[str, datetime | str]) -> str:
        return jwt.encode(to_encode, self.__secret, algorithm=self.__algorithm)

    def __call__(self, user_id: UUID) -> TokenDict:
        access_token = self.__create_token(
            {
                "sub": str(user_id),
                "exp": datetime.now(UTC) + timedelta(minutes=15),
            }
        )

        refresh_token = self.__create_token(
            {
                "sub": str(user_id),
                "exp": datetime.now(UTC) + timedelta(days=15),
            }
        )
        return TokenDict(access_token=access_token, refresh_token=refresh_token)

    def refresh(self, refresh_token: str) -> Optional[str]:
        try:
            payload = jwt.decode(refresh_token, self.__secret, algorithms=[self.__algorithm])
            user = self.repository.get_by_id(UUID(payload.get("sub")))
        except Exception as exc:
            raise ValueError from exc
        if not user:
            return None
        return self.__create_token(
            {
                "sub": str(user),
                "exp": datetime.now(UTC) + timedelta(days=15),
            }
        )

    def getme(self, token: str) -> Optional[User]:
        try:
            payload = jwt.decode(token, self.__secret, algorithms=[self.__algorithm])
            user = self.repository.get_by_id(UUID(payload.get("sub")))
        except Exception as exc:
            raise ValueError from exc
        return user
