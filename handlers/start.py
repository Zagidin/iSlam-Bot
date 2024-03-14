from bot.registar_bot import dp
from aiogram import types
from keyboards.otvet_bot import otvet_botu


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        f"<b>Ас-саляму алейкум "
        f"ва-рахмату-Лла́хи ва-барака́тух @{message.from_user.username}🤚</b>",
        parse_mode='HTML',
        reply_markup=otvet_botu
    )