from uuid import uuid4

from aioredis.client import Redis

from src.exceptions import SlugExpiredError


class LinkGenerator:
    def __init__(self, redis: Redis):
        self._redis = redis

    async def do(self) -> str:
        slug = self._generate_slug()
        await self._save_slug(slug)
        return slug

    def _generate_slug(self) -> str:
        return str(uuid4())

    async def _save_slug(self, slug: str) -> None:
        ttl = 5 * 60
        await self._redis.setex(f'slug:{slug}', ttl, slug)


class DetailRetriever:
    def __init__(self, redis: Redis, slug: str):
        self._redis = redis
        self._slug = slug

    async def do(self):
        if not await self._slug_exists():
            raise SlugExpiredError

        ttl = await self._get_slug_ttl()
        return {'slug': self._slug, 'ttl': ttl, 'visitors': []}

    async def _slug_exists(self) -> bool:
        slug = await self._redis.get(f'slug:{self._slug}')
        return slug == self._slug

    async def _get_slug_ttl(self):
        return await self._redis.ttl(f'slug:{self._slug}')
