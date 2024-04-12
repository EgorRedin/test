from aiogram import Bot, Dispatcher
import asyncio

from handlers import info_handler
from callbacks import callback_handler
import json

API_TOKEN = "7127530696:AAFPZRJo7h0l-xvJXmTyEWbq4WHKXj0noIc"
bot = Bot(token=API_TOKEN)

data = {}


async def send_msg(text):
    await bot.send_message(chat_id=474447825, text=json.dumps(text, ensure_ascii=False))
    data.clear()


func = send_msg


async def main():
    dp = Dispatcher()
    dp.include_routers(
        info_handler.router,
        callback_handler.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
