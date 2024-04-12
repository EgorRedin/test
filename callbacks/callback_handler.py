from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, FSInputFile, InlineKeyboardMarkup


router = Router()


@router.callback_query(F.data.startswith("next"))
async def handle_callback(call: CallbackQuery):
    await call.message.answer("Ознакомился", reply_markup=InlineKeyboardMarkup(inline_keyboard=
                                                                               [
                                                                                   [
                                                                                       InlineKeyboardButton(
                                                                                           text="ДА!",
                                                                                           callback_data="finish")
                                                                                   ]
                                                                               ]))

    await call.answer()


@router.callback_query(F.data.startswith("finish"))
async def handle_finish(call: CallbackQuery):
    photo = FSInputFile(path="./data/photo_2024-04-12_20-26-20.jpg", filename="photo.jpg")
    await call.message.answer_photo(photo, caption="Спасибо за успешную регистрацию")
    await call.answer()

