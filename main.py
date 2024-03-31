import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from config import TOKEN
from db import Database

dp = Dispatcher()
db = Database(db_file="users",
              user="postgres",
              password="mirmakhmudov",
              host='localhost',
              port=5432)


@dp.message(Command("start"))
async def start(message: Message):
    if db.check_user(message.from_user.id):
        await message.answer(f"<b>Xush kelibsiz {message.from_user.full_name}!\nQaytganingiz bilan 🎉</b>")

    else:
        db.add_user(message.from_user.full_name, message.from_user.username, message.from_user.id)
        await message.answer(f"<b>Assalomu alaykum {message.from_user.full_name}!</b>")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
