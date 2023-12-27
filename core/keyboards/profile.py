from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

profile_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text='Назад',
            ),
            KeyboardButton(
                text='Поменять имя',
            ),
        ]
    ],
    resize_keyboard=True,
)
