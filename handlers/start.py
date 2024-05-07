from base.setting_write_base import write_base_settings
from bot.registar_bot import dp
from aiogram import types
from keyboards.otvet_bot import otvet_botu
from base.base_users import (
    open_write_base_users,
    start_base,
)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):

    start_base()

    user_id = write_base_settings()

    if message.from_user.id not in user_id:
        open_write_base_users(message.from_user.id)

    await message.answer(
        f"<b>Ас-саляму алейкум "
        f"ва-рахмату-Лла́хи ва-барака́тух @{message.from_user.username}🤚</b>",
        parse_mode='HTML',
        reply_markup=otvet_botu,
    )
