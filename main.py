import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

from core.middlewares.dbmiddleware import DbSession
from core.settings import settings
from core.utils.dbconnect import create_pool
from core.utils.statesform import StepsForm
from core.handlers.basic import start_chat, go_back
from core.handlers.profile import return_profile, change_username, get_new_username
from core.handlers.give import give_score
from core.handlers.interactives import get_interactive

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
    dp.message.register(start_chat, Command(commands=['start']))
    dp.message.register(give_score, Command(commands=['give']))

    dp.message.register(return_profile, F.text == 'Профиль')
    dp.message.register(change_username, F.text == 'Поменять имя')
    dp.message.register(go_back, F.text == 'Назад')
    dp.message.register(get_interactive, F.text == 'Интерактивы)))')

    dp.message.register(get_new_username, StepsForm.GET_NAME )

    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())