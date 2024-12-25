from aiogram.types import Message

from core.handlers import FEW_SCORE_ERROR_TEXT, USER_BUY_TICKET_TEXT
from core.utils.dbconnect import Request


async def buy_ticket(message: Message, request: Request) -> None:
    score = (await request.get_score(message.from_user.id))[0][0]
    if score < 15:
        await message.answer(FEW_SCORE_ERROR_TEXT)
        return
    number = await request.buy_ticket(message.from_user.id)
    await request.take_score_by_user_id(message.from_user.id, 15)
    await message.answer(USER_BUY_TICKET_TEXT % number)
