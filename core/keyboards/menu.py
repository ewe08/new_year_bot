from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from core import (
    INTERACTIVE_BUTTON_NAME,
    PROFILE_BUTTON_NAME,
    GIVE_SCORE_BUTTON_NAME,
    BUY_TICKET_BUTTON_NAME,
    TAKE_SCORE_BUTTON_NAME,
)

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text=INTERACTIVE_BUTTON_NAME,
            ),
            KeyboardButton(
                text=PROFILE_BUTTON_NAME,
            ),
        ],
        [
            KeyboardButton(
                text=BUY_TICKET_BUTTON_NAME,
            ),
        ],
    ],
    resize_keyboard=True,
)

giver_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text=INTERACTIVE_BUTTON_NAME,
            ),
            KeyboardButton(
                text=PROFILE_BUTTON_NAME,
            ),
        ],
        [
            KeyboardButton(
                text=BUY_TICKET_BUTTON_NAME,
            ),
        ],
        [
            KeyboardButton(
                text=GIVE_SCORE_BUTTON_NAME,
            ),
        ],
    ],
    resize_keyboard=True,
)


admin_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text=INTERACTIVE_BUTTON_NAME,
            ),
            KeyboardButton(
                text=PROFILE_BUTTON_NAME,
            ),
        ],
        [
            KeyboardButton(
                text=BUY_TICKET_BUTTON_NAME,
            ),
        ],
        [
            KeyboardButton(
                text=GIVE_SCORE_BUTTON_NAME,
            ),
        ],
        [
            KeyboardButton(
                text=TAKE_SCORE_BUTTON_NAME,
            ),
        ],
    ],
    resize_keyboard=True,
)
