from bot.registar_bot import dp
from aiogram.types import Message, ContentType, ReplyKeyboardRemove
from base.setting_write_base import write_base_settings
from aiogram.dispatcher import FSMContext
from fsm.sms_feedback import Userfeedback
from keyboards.phone_number import phone
from base.base_users import (
    open_write_base_users,
    start_base,
)


@dp.message_handler(commands=['feedback'])
async def feedback(message: Message):

    start_base()

    user_id = write_base_settings()

    if message.from_user.id not in user_id:
        await message.answer(
            text=f"Напишитие сообщение, "
                 f"которое хотите отправить Администратору "
                 f"Телеграм Бота ..."
        )

        await Userfeedback.sms_feedback.set()
    else:
        await message.answer(
            text=f"Обратную связь можно оставить только один раз! 😔\n"
                 f"\nP.S. Можно будет написать Администратору через 48 часов 😌",
            reply_markup=ReplyKeyboardRemove()
        )


@dp.message_handler(state=Userfeedback.sms_feedback)
async def send_feedback(message: Message, state: FSMContext):

    async with state.proxy() as data:
        data['sms_feedback'] = message.text

    await message.answer(
        text=f"Поделитесь, номером телефона, чтоб Администратор мог с Вами связаться",
        reply_markup=phone
    )

    await Userfeedback.next()


@dp.message_handler(state=Userfeedback.phone, content_types=ContentType.CONTACT)
async def send_phone_feedback(message: Message, state: FSMContext):

    async with state.proxy() as data:
        data['phone_feedback'] = message.contact.phone_number

    await state.finish()

    open_write_base_users(
        id_user=message.from_user.id,
        name='https://t.me/' + message.from_user.username,
        phone=data['phone_feedback'],
        sms_user=data['sms_feedback']
    )

    await message.answer(
        text="Спасибо за обратную связь 😉📝",
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        text="Администратор скоро свяжется с Вами ☎"
    )
