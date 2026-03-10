import asyncpg
from app.config import settings


class Database:
    def __init__(self):
        self.pool: asyncpg.pool.Pool | None = None

    async def connect(self):
        dsn = (
            f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
            f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
        )

        self.pool = await asyncpg.create_pool(dsn=dsn)

    async def close(self):
        if self.pool:
            await self.pool.close()


db = Database()