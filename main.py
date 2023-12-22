import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

from core.middlewares.dbmiddleware import DbSession
from core.settings import settings
from core.utils.dbconnect import create_pool
from core.handlers.basic import start_chat
from core.handlers.profile import return_profile

async def start():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - [%(levelname)s] - %(name)s - '
               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
    )
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    await bot.delete_webhook(drop_pending_updates=True)

    pull_connect = await create_pool()

    dp = Dispatcher()
    dp.update.middleware.register(DbSession(pull_connect))
    # dp.startup.register(start_bot)
    dp.message.register(start_chat, Command(commands=['start']))
    dp.message.register(return_profile, Command(commands=['settings']))

    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())