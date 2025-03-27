from typing import Optional

from pydantic import Field, NonNegativeInt, PositiveFloat, PositiveInt
from pydantic_settings import BaseSettings

class RedisConfig(BaseSettings):
    REDIS_HOST: str = Field(
        default="localhost",
    )

    REDIS_PORT: PositiveInt = Field(
        default=6379,
    )
        
    REDIS_USERNAME: Optional[str] = Field(
        default=None,
    )

    REDIS_PASSWORD: Optional[str] = Field(
        default=None,
    )

    REDIS_DB: NonNegativeInt = Field(
        default=0,
    )

    REDIS_USE_SSL: bool = Field(
        default=False,
    )