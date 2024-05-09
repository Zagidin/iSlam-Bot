from bot.registar_bot import dp
from aiogram import types
from keyboards.keyboard_surah.all_surah import all_surah


@dp.message_handler(commands=['surah'])
async def surah(message: types.Message):
    await message.answer(text='Выберите Суру', reply_markup=all_surah)
