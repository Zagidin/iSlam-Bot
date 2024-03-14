from bot.registar_bot import dp
from aiogram.utils import executor


def starts_bot():
    executor.start_polling(dp, skip_updates=True)
