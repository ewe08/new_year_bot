from aiogram.types import Message
from aiogram.methods.send_message import SendMessage
from core.settings import settings
from core.utils.dbconnect import Request


async def handle_input(message: Message, request: Request):
    if not message.from_user.id in settings.admins:
        await message.reply('Эта фича только для подопечных деда мороза хихихи')
    else:
        args = message.text.split()
        username = ' '.join(args[2:])
        user_id = (await (request.check_username(username)))[0][0]
        value = int(args[1])
        return value, user_id, username


async def give_score(message: Message, request: Request):
    value, user_id, username = await handle_input(message, request)
    await request.give_score_by_username(
        username,
        value,
    )
    await message.answer('Гроши отправлены!')

    await SendMessage(text='Дед мороз дал вам гроши', chat_id=user_id)
