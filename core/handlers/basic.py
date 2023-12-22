from aiogram.types import Message

from core.utils.dbconnect import Request

async def start_chat(message: Message, request: Request):
    await message.reply('ДОбро пожаловать на Новый год в ПУНКЕ!!!! ВСЕХ С НГ!!')
    await request.register_user(
        message.from_user.id,
        message.from_user.username,
    )


