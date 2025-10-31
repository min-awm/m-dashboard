from fastapi import APIRouter

from auth.api import auth_api

router = APIRouter(prefix="/api/auth")
router.include_router(auth_api.router)
