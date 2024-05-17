from typing import Optional

from passlib.context import CryptContext

from app.core.domain import Repository, User

from .schemas import UserIn, UserLogin


class SignIn:
    def __init__(self, repository: Repository[UserIn, User]) -> None:
        self.repository = repository

    def __call__(self, user_login: UserLogin) -> Optional[User]:
        user = self.repository.get_by(email=user_login.email)
        if not user:
            return None
        pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
        if not pwd_context.verify(
            user_login.password.get_secret_value(),
            user.hashed_password.get_secret_value(),
        ):
            return None
        return user
