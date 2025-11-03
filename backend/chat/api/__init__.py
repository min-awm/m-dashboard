from fastapi import APIRouter

from chat.api import chat_api

router = APIRouter(prefix="/api/chat")
router.include_router(chat_api.router)
