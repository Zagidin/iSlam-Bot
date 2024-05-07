import os

from bot.registar_bot import dp
from aiogram.types import Message, ReplyKeyboardRemove
from dotenv import load_dotenv
from keyboards.keyboard_admin.sms_users import smsusers
from aiogram.dispatcher import FSMContext
from fsm.admins import Admins


load_dotenv()


@dp.message_handler(commands=['admin'])
async def admin(message: Message):

    await message.answer(
        text="**** Введите Пароль ****",
    )

    await Admins.admin_password.set()


@dp.message_handler(state=Admins.admin_password)
async def admin_password(message: Message, state: FSMContext):

    async with state.proxy() as data:
        data['admin_password'] = message.text

    await state.finish()

    if data['admin_password'] == os.getenv('ADMIN_PASSWORD'):
        await message.answer(
            text="Ас-саляму алейкум ва-рахмату-Ллахи ва-баракатух Загидин",
            reply_markup=smsusers
        )
    else:
        await message.answer(
            text="**** !Неверный пароль! ****",
            reply_markup=ReplyKeyboardRemove()
        )
