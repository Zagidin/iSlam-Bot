import os

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()

bot = Bot(token=os.getenv('TOKEN_BOT'))
dp = Dispatcher(bot=bot, storage=MemoryStorage())
