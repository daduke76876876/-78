import asyncio

from aiogram import Bot
from aiogram import Dispatcher

from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.profile import router as profile_router
from handlers.cover import router as cover_router

from database.db import init_db


async def main():

    await init_db()

    bot = Bot(BOT_TOKEN)

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(profile_router)
    dp.include_router(cover_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
