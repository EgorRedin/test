from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    name = State()
    phone_number = State()
    comment = State()
