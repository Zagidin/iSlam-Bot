from bot.registar_bot import dp
from aiogram import types
from inlanekey.nasheed_key import nasheed_btn


@dp.message_handler(commands=['nasheed'])
async def nas1heed_song(message: types.Message):
    await message.answer(
        'Выберите плейлисты предложенные снизу 🔊',
        reply_markup=nasheed_btn
    )
