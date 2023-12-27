from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text='Интерактивы)))',
            ),
            KeyboardButton(
                text='Профиль',
            ),
        ]
    ],
    resize_keyboard=True,
)
