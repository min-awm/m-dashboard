from typing import Type

from beanie import Document

from auth.model.user import User


class UserRepository:
    def __init__(self, model: Type[Document] = User):
        self.model = model

    async def create_user(self, **kwargs) -> User:
        user = self.model(**kwargs)
        await user.insert()
        return user
    
    async def get_user_by_username(self, username: str) -> User:
        return await self.model.find_one(User.username == username)

