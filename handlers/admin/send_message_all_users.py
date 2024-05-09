from bot.registar_bot import dp, bot
from aiogram.types import Message
from base.base_users import select_all_users


@dp.message_handler(commands=['send_all'])
async def send_all_message(message: Message):

    if message.from_user.id == 6128986459:
        text = message.text[10:]
        user_id = select_all_users()

        for el in user_id:
            await bot.send_message(el[0], text)
