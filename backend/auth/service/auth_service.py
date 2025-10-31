from uuid import UUID

from core.service import BaseService
from fastapi import Request
from pwdlib import PasswordHash

from auth.api.schemas import LoginSchema, RegisterSchema
from auth.helper.token import create_access_token, create_refresh_token
from auth.model.user import STATUS
from auth.repository.user_repository import UserRepository

password_hash = PasswordHash.recommended()


class AuthService(BaseService):
    def __init__(self, request: Request, user_repo: UserRepository):
        self.request = request
        self.user_repo = user_repo

    async def register(self, data: RegisterSchema):
        """Register for user and return user info"""
        password = password_hash.hash(data.password)
        user = await self.user_repo.create_user(
            name=data.name,
            username=data.username,
            password=password,
            status=STATUS.active,
        )

        return self.response_success(
            {
                "user": {
                    "name": user.name,
                    "username": user.username,
                    "status": user.status,
                },
                "msg": "User created successfully",
            },
        )

    async def login(self, data: LoginSchema):
        """Login for user and return user info, access token"""
        user = await self.user_repo.get_user_by_username(data.username)
        if not user:
            return self.exception("Invalid username or password")

        if not password_hash.verify(data.password, user.password):
            return self.exception("Invalid username or password")

        if user.status == STATUS.inactive:
            return self.exception("User is inactive")

        access_token = create_access_token(user.uuid)
        refresh_token = create_refresh_token(user.uuid)

        return self.response_success(
            {
                "token": {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                },
                "msg": "Login successfully",
            },
        )

    async def get_me(self):
        """Login for user and return user info, access token"""
        user_uuid = self.request.state.user_uuid
        user = await self.user_repo.get_user_by_uuid(UUID(user_uuid))

        return self.response_success(
            {
                "user": {
                    "name": user.name,
                    "username": user.username,
                    "status": user.status,
                },
            },
        )
