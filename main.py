import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command

from core import *
from core.handlers.admins import take_score, request_remove_score
from core.handlers.tickets import buy_ticket
from core.middlewares.dbmiddleware import DbSession
from core.settings import settings
from core.utils.dbconnect import create_pool
from core.utils.statesform import StepsForm, GiveScoreForm, TakeScoreForm
from core.handlers.basic import start_chat, go_back
from core.handlers.profile import return_profile, change_username, get_new_username
from core.handlers.give import give_score, request_score
from core.handlers.interactives import get_interactive

async def start():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - [%(levelname)s] - %(name)s - '
               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
    )
    bot = Bot(token=settings.bots.bot_token, default=DefaultBotProperties(parse_mode='HTML'))
    await bot.delete_webhook(drop_pending_updates=True)

    loop = asyncio.get_event_loop()
    pull_connect = await create_pool(loop)

    dp = Dispatcher()
    dp.update.middleware.register(DbSession(pull_connect))

    dp.message.register(start_chat, Command(commands=['start']))

    dp.message.register(return_profile, F.text == PROFILE_BUTTON_NAME)
    dp.message.register(change_username, F.text == CHANGE_NAME_BUTTON_NAME)
    dp.message.register(go_back, F.text == BACK_BUTTON_NAME)
    dp.message.register(get_interactive, F.text == INTERACTIVE_BUTTON_NAME)
    dp.message.register(request_score, F.text == GIVE_SCORE_BUTTON_NAME)
    dp.message.register(request_remove_score, F.text == TAKE_SCORE_BUTTON_NAME)
    dp.message.register(buy_ticket, F.text == BUY_TICKET_BUTTON_NAME)

    dp.message.register(get_new_username, StepsForm.GET_NAME )
    dp.message.register(give_score, GiveScoreForm.GET_USERNAME)
    dp.message.register(take_score, TakeScoreForm.GET_USERNAME)

    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
