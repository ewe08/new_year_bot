from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.utils.dbconnect import Request
from core.utils.statesform import StepsForm
from core.keyboards.profile import profile_keyboard
from core.keyboards.menu import menu_keyboard


async def return_profile(message: Message, request: Request):
    data = (await request.get_userdata(message.from_user.id))[0]
    await message.answer(
        f"Ваш профиль:\nОчки: {data[0][0]}\nВаше имя: {data[0][1]}", 
        reply_markup=profile_keyboard
    )

async def change_username(message: Message, state: FSMContext):
    await message.answer(f"Введите новое имя:")
    await state.set_state(StepsForm.GET_NAME)

async def get_new_username(message: Message, request: Request, state: FSMContext):
    #data = (await request.check_username(message.text))[0]
    #if data[0]:
    await request.update_username(message.from_user.id, message.text)
    await message.answer(f"Вы успешно поменяли имя на {message.text}", reply_markup=menu_keyboard)
    await state.clear()
    #else:
        #await message.answer(f"Этот ник уже занят")
        #await change_username(message, state)
