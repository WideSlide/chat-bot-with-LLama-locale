import asyncio
from aiogram import Bot, Dispatcher, types
from handlers.user_private import user_private
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)

dp = Dispatcher()

dp.include_router(user_private)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())






