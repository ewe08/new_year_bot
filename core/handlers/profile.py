from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.handlers import PROFILE_TEXT
from core.utils.dbconnect import Request
from core.utils.statesform import StepsForm
from core.utils.utils import get_keyboard
from core.keyboards.profile import profile_keyboard


async def return_profile(message: Message, request: Request):
    score = (await request.get_score(message.from_user.id))[0][0]
    username = (await request.get_username(message.from_user.id))[0][0]
    tickets = await request.get_tickets(message.from_user.id)
    if tickets:
        tickets = ' '.join([str(el[0]) for el in tickets])
    else:
        tickets = 'У вас нет пока билетов. Скорее купите их'
    await message.answer(
        PROFILE_TEXT % (score, username, tickets),
        reply_markup=profile_keyboard
    )

async def change_username(message: Message, state: FSMContext):
    await message.answer(f"Введите новое имя:")
    await state.set_state(StepsForm.GET_NAME)

async def get_new_username(message: Message, request: Request, state: FSMContext):
    data = (await request.check_username(message.text))
    if not data:
        await request.update_username(message.from_user.id, message.text)
        await message.answer(f"Вы успешно поменяли имя на {message.text}", reply_markup=await get_keyboard(message.from_user.id))
        await state.clear()
    else:
        await message.answer(f"Этот ник уже занят")
        await change_username(message, state)
