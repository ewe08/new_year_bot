from aiogram.types import Message

from core.handlers import (
    WELCOME_MESSAGE_TEXT,
    MAIN_MENU_MESSAGE_TEXT,
)
from core.utils.dbconnect import Request
from core.utils.utils import get_keyboard


async def start_chat(message: Message, request: Request):
    await message.reply(
        WELCOME_MESSAGE_TEXT,
        reply_markup=await get_keyboard(message.from_user.id),
    )
    await request.register_user(
        message.from_user.id,
        message.from_user.username,
    )


async def go_back(message: Message):
    await message.answer(MAIN_MENU_MESSAGE_TEXT, reply_markup=await get_keyboard(message.from_user.id))
