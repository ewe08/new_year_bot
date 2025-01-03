from typing import Callable, Awaitable, Dict, Any

import aiomysql
from aiogram import BaseMiddleware
from aiogram.types import Message

from core.utils.dbconnect import Request


class DbSession(BaseMiddleware):
    def __init__(self, connector: aiomysql.pool.Pool):
        super().__init__()
        self.connector = connector

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        async with self.connector.acquire() as connect:
            data['request'] = Request(connect)
            return await handler(event, data)
