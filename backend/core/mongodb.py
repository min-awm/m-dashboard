from auth.model.user import User
from beanie import init_beanie
from pymongo import AsyncMongoClient

from core.config import get_settings

settings = get_settings()


async def init_db():
    client = AsyncMongoClient(settings.MONGO_URI)

    document_models = [User]

    await init_beanie(
        database=client[settings.MONGO_DB_NAME], document_models=document_models
    )