from bot.registar_bot import dp
from aiogram.utils import executor


def starts_bot():
    print('\nБот запущен!\nВсе Обновления были успешно пропущены: ', end='')
    executor.start_polling(dp, skip_updates=True)
    print('\nБот остановлен! ', end='')
