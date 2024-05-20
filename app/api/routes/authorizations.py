import re
from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import SecretStr
from sqlalchemy.exc import IntegrityError

from app.core.domain import TokenDict, User
from app.core.use_cases.auth.schemas import UserIn, UserLogin

from ..dependencies.api_security_service import ApiSecurityService
from ..dependencies.api_signin import APISignIn
from ..dependencies.api_signup import APISignUp
from ..dependencies.jwt import (ACCESS_TOKEN_EXPIRE_MINUTES, Token,
                                authenticate_user, create_access_token,
                                fake_users_db)

router = APIRouter()


@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    """Login for access token and refresh token

    Args:
        form_data (OAuth2PasswordRequestForm): OAuth2PasswordRequestForm
    Returns:
        Token: Token
    Raises:
        HTTPException: HTTPException
    """

    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return Token(access_token=access_token, token_type="bearer")


@router.post("/signup", response_model=User)
async def signup(user_in: UserIn, api_signup: APISignUp = Depends()):
    try:
        return api_signup(user_in)
    except IntegrityError as error:
        error_message = re.findall(r"DETAIL:  (.*)", str(error))[0]
        error_message = re.sub(r"Key \((.*)\)=\(", "", error_message).replace(")", "")
        raise HTTPException(status_code=400, detail=error_message) from error
    except Exception as error:
        raise HTTPException(status_code=409, detail=repr(error)) from error


@router.post("/signin", response_model=TokenDict)
async def signin(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    security_service: Annotated[ApiSecurityService, Depends()],
    api_signin: Annotated[APISignIn, Depends()],
) -> TokenDict:
    user_login = UserLogin(
        email=form_data.username,
        password=SecretStr(form_data.password),
    )
    user = api_signin(user_login)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return security_service(user.uuid)


@router.get("/refresh")
async def refresh_token(
    Authorization: Annotated[str | None, Header()],
    security_service: Annotated[ApiSecurityService, Depends()],
):
    if Authorization is None or not Authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Refresh token not found")
    refreshed_token = Authorization.split(" ")[1]
    new_token = security_service.refresh(refreshed_token)
    if not new_token:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    return {"access_token": new_token}
