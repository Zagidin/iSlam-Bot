from bot.registar_bot import dp
from aiogram.types import Message
from keyboards.keyboard_admin.sms_users import smsusers


@dp.message_handler(commands=['admin'])
async def admin(message: Message):
    await message.answer(
        text="Админ",
        reply_markup=smsusers
    )