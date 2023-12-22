from aiogram.types import Message

from core.utils.dbconnect import Request

async def return_profile(message: Message, request: Request):
    data = (await request.get_userdata(message.from_user.id))[0]
    await message.answer(f"Ваш профиль:\nОчки:{data[0][0]}\nВаше имя: {data[0][1]}")
    