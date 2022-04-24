import aioredis

from src.settings import settings


def get_redis_client():
    return aioredis.from_url(settings.redis_url, decode_responses=True)
