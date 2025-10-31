from datetime import datetime, timedelta, timezone
from uuid import UUID

import jwt
from core.config import get_settings
from core.redis import get_redis_client
from jwt import PyJWTError

from auth.enum.token_type import TokenType

redis_client = get_redis_client()
settings = get_settings()

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM_JWT
ACCESS_TOKEN_EXPIRE = settings.ACCESS_TOKEN_EXPIRE
REFRESH_TOKEN_EXPIRE = settings.REFRESH_TOKEN_EXPIRE

ACCESS_TOKEN_REDIS_EXPIRE = ACCESS_TOKEN_EXPIRE * 60
REFRESH_TOKEN_REDIS_EXPIRE = REFRESH_TOKEN_EXPIRE * 60 * 60 * 24


def decode_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except PyJWTError:
        return None


def encode_token(payload: dict) -> str:
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def create_access_token(user_uuid: UUID):
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE)
    to_encode = {"sub": str(user_uuid), "type": TokenType.access, "exp": expire}
    access_token = encode_token(to_encode)
    redis_client.set("auth:access_token", access_token, ex=ACCESS_TOKEN_REDIS_EXPIRE)
    return access_token


def create_refresh_token(user_uuid: UUID):
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE)
    to_encode = {"sub": str(user_uuid), "type": TokenType.refresh, "exp": expire}
    refresh_token = encode_token(to_encode)
    redis_client.set("auth:refresh_token", refresh_token, ex=REFRESH_TOKEN_REDIS_EXPIRE)

    return refresh_token
