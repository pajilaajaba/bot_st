import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from apps.get_info_handl import router
from apps.database.models import async_main

load_dotenv()
password = os.getenv("Password")

async def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    await async_main()
    dp.include_router(router)
    await dp.start_polling(bot)

    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot off")