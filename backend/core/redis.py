from functools import lru_cache

import redis

from core.config import get_settings

settings = get_settings()


@lru_cache()
def get_redis_client() -> redis.Redis:
    return redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        password=settings.REDIS_PASSWORD,
        decode_responses=True,
    )
