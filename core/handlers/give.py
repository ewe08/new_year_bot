from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.methods.send_message import SendMessage

from core.handlers import (
    GIVE_SCORE_MESSAGE_TEXT,
    GIVER_SUCCESS_SEND_SCORE_MESSAGE_TEXT,
    USER_SUCCESS_GET_SCORE_TEXT,
    USER_NOT_FOUNT_ERROR_TEXT,
    INCORRECT_SCORE_ERROR_TEXT,
)
from core.utils.utils import check_giver, check_admin
from core.utils.dbconnect import Request
from core.utils.exceptions import IncorrectScoreError, UserNotFoundError
from core.utils.statesform import GiveScoreForm


async def handle_input(message: Message, data: str, request: Request):
    username, value = data.split()
    user_id = (await (request.check_username(username)))

    if not user_id:
        await message.answer(USER_NOT_FOUNT_ERROR_TEXT)
        raise UserNotFoundError()

    if not (1 <= int(value) <= 5) and not await check_admin(message.from_user.id):
        await message.answer(INCORRECT_SCORE_ERROR_TEXT)
        raise IncorrectScoreError()

    if (message.from_user.id == user_id[0][0]) and not await check_admin(message.from_user.id):
        await message.answer('э ты кого наебать хочешь самый умный типа?')
        return

    return value, user_id[0][0], username


async def request_score(message: Message, state: FSMContext):
    if not await check_giver(message.from_user.id):
        return

    await message.answer(GIVE_SCORE_MESSAGE_TEXT)
    await state.set_state(GiveScoreForm.GET_USERNAME)


async def give_score(message: Message, request: Request, state: FSMContext, bot: Bot):
    value, user_id, username = await handle_input(message, message.text, request)
    await state.clear()
    await request.give_score_by_username(
        username,
        value,
    )
    await message.answer(GIVER_SUCCESS_SEND_SCORE_MESSAGE_TEXT)
    await bot(SendMessage(text=USER_SUCCESS_GET_SCORE_TEXT, chat_id=user_id))
