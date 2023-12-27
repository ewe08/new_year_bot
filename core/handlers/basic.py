from aiogram.types import Message

from core.utils.dbconnect import Request
from core.keyboards.menu import menu_keyboard

async def start_chat(message: Message, request: Request):
    await message.reply(
        'ДОбро пожаловать на Новый год в ПУНКЕ!!!! ВСЕХ С НГ!!',
        reply_markup=menu_keyboard,
    )
    await request.register_user(
        message.from_user.id,
        message.from_user.username,
    )


async def go_back(message: Message):
    await message.answer('Главное меню', reply_markup=menu_keyboard)
