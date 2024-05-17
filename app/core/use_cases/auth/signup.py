from app.core.domain.repository import Repository
from app.core.domain.user import User

from .schemas import UserIn


class SignUp:
    def __init__(self, repository: Repository[UserIn, User]) -> None:
        self.repository = repository

    def __call__(self, user_in: UserIn) -> User:
        return self.repository.create(user_in)
