import asyncio
import logging
from aiogram import Bot, Dispatcher
import config
from database.models import init_db
from handlers import admin, admin_panel, common, master

logging.basicConfig(level=logging.INFO)


async def main():
    await init_db()

    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(admin_panel.router)
    dp.include_router(common.router)
    dp.include_router(master.router)
    dp.include_router(admin.router)

    logging.info("Starting Telegram Bot Polling...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
