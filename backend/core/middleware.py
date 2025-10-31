from auth.helper.token import decode_token
from auth.enum.token_type import TokenType
from fastapi import Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from core.config import get_settings

settings = get_settings()

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM_JWT


class Middleware(BaseHTTPMiddleware):
    """JWT middleware to verify token and set user info to request state"""

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        if request.url.path in [
            "/docs",
            "/openapi.json",
            "/api/auth/register",
            "/api/auth/login",
            "/api/auth/access-token",
        ]:
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        if auth_header is None or not auth_header.startswith("Bearer "):
            return JSONResponse(
                status_code=401,
                content={"detail": {"msg": "Invalid token"}},
            )

        token = auth_header.split(" ")[1]
        payload = decode_token(token)
        \
        if payload is None:
            return JSONResponse(status_code=401, content={"detail": {"msg": "Invalid token"}})

        if payload["type"] != TokenType.access:
            return JSONResponse(status_code=401, content={"detail": {"msg": "Invalid token"}})
        
        request.state.user_uuid = payload["sub"]
        response = await call_next(request)
        return response
