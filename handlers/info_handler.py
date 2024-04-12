from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, FSInputFile, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from States.states import Form
import re
from main import data, func

router = Router()


@router.message(Command("start"))
async def start_cmd(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer(f"{message.from_user.username}, Добро пожаловать в компанию DamnIT")
    await message.answer("Напишите свое ФИО")


@router.message(Form.name)
async def handle_name(message: Message, state: FSMContext):
    if re.search(r'\d', message.text):
        await message.answer("ФИО не должно содержать цифры")
    else:
        await state.update_data(name=message.text)
        await state.set_state(Form.phone_number)
        await message.answer("Укажите Ваш номер телефона - в формате 7 999 999 99 99")


@router.message(Form.phone_number)
async def handle_phone(message: Message, state: FSMContext):
    if re.search(r'^7\s9\d{2}\s\d{3}\s\d{2}\s\d{2}$', message.text):
        await state.update_data(phone_number=message.text)
        await state.set_state(Form.comment)
        await message.answer("Напишите любой комментарий")
    else:
        await message.answer("Номер телефона введен не в том формате (формат 7 999 999 99 99)")


@router.message(Form.comment)
async def handle_comment(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)
    info = await state.get_data()
    data.update(info)
    await func(data)
    await state.clear()
    file = FSInputFile(path="./data/test.pdf", filename="test.pdf")
    await message.answer_document(file, caption="Последний шаг! Ознакомься с вводными "
                                                                      "положениями",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text="Далее", callback_data="next")
                                      ]
                                  ]))
