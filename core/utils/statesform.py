from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_NAME = State()


class GiveScoreForm(StatesGroup):
    GET_USERNAME = State()


class TakeScoreForm(StatesGroup):
    GET_USERNAME = State()
