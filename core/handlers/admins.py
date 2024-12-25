from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.methods import SendMessage
from aiogram.types import Message

from core.handlers import (
    ADMIN_TAKE_SCORE_MESSAGE_TEXT,
    ADMIN_SUCCESS_TAKE_SCORE_MESSAGE_TEXT,
    USER_SUCCESS_LOSE_SCORE_TEXT,
)
from core.utils.dbconnect import Request
from core.utils.statesform import TakeScoreForm
from core.utils.utils import check_admin


async def handle_input(data: str, request: Request):
    username, value = data.split()
    user_id = (await (request.check_username(username)))

    return value, user_id[0][0], username


async def request_remove_score(message: Message, state: FSMContext):
    if not await check_admin(message.from_user.id):
        return

    await message.answer(ADMIN_TAKE_SCORE_MESSAGE_TEXT)
    await state.set_state(TakeScoreForm.GET_USERNAME)


async def take_score(message: Message, request: Request, state: FSMContext, bot: Bot):
    value, user_id, username = await handle_input(message.text, request)
    await state.clear()
    await request.take_score_by_username(
        username,
        value,
    )
    await message.answer(ADMIN_SUCCESS_TAKE_SCORE_MESSAGE_TEXT)
    await bot(SendMessage(text=USER_SUCCESS_LOSE_SCORE_TEXT, chat_id=user_id))
