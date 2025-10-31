from typing import Annotated
from fastapi import APIRouter, Depends
from pwdlib import PasswordHash

from auth.api.schemas import LoginSchema, RegisterSchema
from auth.dependencies import get_auth_service
from auth.service.auth_service import AuthService

router = APIRouter(tags=["auth"])
password_hash = PasswordHash.recommended()


@router.post("/register")
async def register(
    data: RegisterSchema,
    service: Annotated[AuthService, Depends(get_auth_service)],
):
    """Register for user"""
    return await service.register(data)


@router.post("/login")
async def login(
    data: LoginSchema,
    service: Annotated[AuthService, Depends(get_auth_service)],
):
    """Login for user"""
    return await service.login(data)

@router.get("/me")
async def get_me(
    service: Annotated[AuthService, Depends(get_auth_service)],
):
    """Get user info"""
    return await service.get_me()
