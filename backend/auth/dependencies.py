from typing import Annotated

from fastapi import Depends, Request

from auth.repository.user_repository import UserRepository
from auth.service.auth_service import AuthService


def get_user_repository() -> UserRepository:
    return UserRepository()


def get_auth_service(
    request: Request,
    repo: Annotated[UserRepository, Depends(get_user_repository)],
) -> AuthService:
    return AuthService(request, repo)
