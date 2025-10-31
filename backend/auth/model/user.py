from enum import Enum
from uuid import UUID, uuid4

from beanie import Document
from pydantic import Field


class STATUS(str, Enum):
    active = "ACTIVE"
    inactive = "INACTIVE"


class User(Document):
    uuid: UUID = Field(default_factory=uuid4)
    name: str
    username: str
    password: str
    status: STATUS

    class Settings:
        name = "users"
