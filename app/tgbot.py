from aiogram import Bot, Dispatcher, types, Router
import asyncio
from app.handlers import router
from app.parser import parsing

async def start():
    parsing()
    bot = Bot(token = '7299361034:AAGOekebelrRoXoWRXn9bRq36_ND0EtJtaU')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

def startbot():
    asyncio.run(start())