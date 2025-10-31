from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # ====== MongoDB ======
    MONGO_URI: str = Field(env="MONGO_URI")
    MONGO_DB_NAME: str = Field(env="MONGO_DB_NAME")

    # ====== JWT ======
    SECRET_KEY: str = Field(env="SECRET_KEY")
    ALGORITHM_JWT: str = Field(env="ALGORITHM_JWT")
    ACCESS_TOKEN_EXPIRE: int = Field(env="ACCESS_TOKEN_EXPIRE")
    REFRESH_TOKEN_EXPIRE: int = Field(env="REFRESH_TOKEN_EXPIRE")

    # ====== Redis ======
    REDIS_HOST: str = Field(env="REDIS_HOST")
    REDIS_PASSWORD: str = Field(env="REDIS_PASSWORD")
    REDIS_PORT: int = Field(env="REDIS_PORT")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache()
def get_settings() -> Settings:
    return Settings()
