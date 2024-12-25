from aiogram.types import Message


async def get_interactive(message: Message):
    await message.answer(
        '✨ <b>У нас в программе:</b> ✨\n\n'
        '🔮 Таро и гадания\n'
        '🎟️ Лотерея\n'
        '📬 Создание новогодней открытки\n'
        '📜 Искусство оригами\n'
        '💅 Накрась ноготки\n'
        '🎄 Испытание гринча\n'
        '🎨 Поделки своими руками\n'
        '👩‍🎤 Фантазийный грим'
        )
