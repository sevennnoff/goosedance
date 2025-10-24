from aiogram import Dispatcher, Bot
import asyncio
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from handlers import router
from dotenv import load_dotenv
import os


load_dotenv(override=True)

bot = Bot(token=os.getenv("BOT_API_TOKEN"), default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher(storage=MemoryStorage())

async def main():
    dp.include_router(router=router)
    await dp.start_polling(bot)

if  __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopped Successfully")
