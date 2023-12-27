from aiogram.types import Message


async def get_interactive(message: Message):
    await message.answer(
        'У нас в программе: \n' \
        'Стихотворение Деду Морозу\n'\
        'Плетение из резиночек\n'\
        'Новогодняя открытка\n'\
        'Оригами\n'\
        'Накрась ноготки\n'\
        'Твистер\n'\
        'Дартс\n'\
        'Повтори фото\n'\
        'Грим'
        )
