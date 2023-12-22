import asyncpg

from core.settings import settings


async def create_pool():
    return await asyncpg.create_pool(
        user=settings.databases.user,
        password=settings.databases.password,
        database=settings.databases.database,
        host=settings.databases.host,
        port=settings.databases.port,
        command_timeout=settings.databases.command_timeout,
    )

def double_quote(string):
    if string is None:
        return string
    return string.replace("'", "''")

class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def register_user(self, user_id, username):
        query = f"INSERT INTO datauser (id, username, score) " \
                f"VALUES ({user_id}, '{double_quote(username)}', 0)" 
        await self.connector.execute(query)
    
    async def get_userdata(self, user_id):
        query = f"SELECT (score, username) FROM datauser WHERE id={user_id}"
        return await self.connector.fetch(query)
