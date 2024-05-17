from pydantic import BaseModel


class TokenDict(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"
