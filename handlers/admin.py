import os

from bot.registar_bot import dp, bot
from aiogram.types import Message, ReplyKeyboardRemove
from dotenv import load_dotenv
from keyboards.keyboard_admin.admin_users import admin_users
from aiogram.dispatcher import FSMContext
from fsm.admins import Admins
from base.base_users import select_all_users


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
            reply_markup=admin_users
        )
        await message.answer(text="Выберите команду ...")
    else:
        await message.answer(
            text="**** !Неверный пароль! ****",
            reply_markup=ReplyKeyboardRemove()
        )


@dp.message_handler(commands=['send_all'])
async def send_all_message(message: Message):

    if message.from_user.id == 6128986459:
        text = message.text[10:]
        user_id = select_all_users()

        for el in user_id:
            await bot.send_message(el[0], text)
