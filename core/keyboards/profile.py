from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from core import (
    BACK_BUTTON_NAME,
    CHANGE_NAME_BUTTON_NAME,
)

profile_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text=BACK_BUTTON_NAME,
            ),
            KeyboardButton(
                text=CHANGE_NAME_BUTTON_NAME,
            ),
        ]
    ],
    resize_keyboard=True,
)
