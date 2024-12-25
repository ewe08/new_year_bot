from aiogram.types import ReplyKeyboardMarkup

from core.keyboards.menu import (
    admin_keyboard,
    giver_keyboard,
    menu_keyboard,
)
from core.settings import settings


async def check_giver(user_id: int) -> bool:
    if user_id in settings.givers:
        return True
    return False


async def check_admin(user_id: int) -> bool:
    if user_id in settings.admins:
        return True
    return False


async def get_keyboard(user_id: int) -> ReplyKeyboardMarkup:
    if await check_admin(user_id):
        return admin_keyboard
    elif await check_giver(user_id):
        return giver_keyboard
    return menu_keyboard
