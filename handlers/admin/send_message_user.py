from bot.registar_bot import dp, bot
from aiogram.types import Message
from fsm.admins import MessageUsers
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=['message'])
async def send_message(message: Message):
    if message.from_user.id == 6128986459:
        await message.answer(
            text="Напишите   <u><b>User-ID</b></u>  пользователя: ",
            parse_mode='HTML'
        )

        await MessageUsers.user_id.set()


@dp.message_handler(state=MessageUsers.user_id)
async def send_message(message: Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['user_id'] = int(message.text)

        await message.answer(
            text="Напишите сообщение пользователю ..."
        )

        await MessageUsers.next()
    except:
        await state.finish()
        await message.answer(
            text="Вы ввели неправильный ID пользователя! 😟\n"
                 "Попробуйте повторить отправку /message"
        )


@dp.message_handler(state=MessageUsers.message)
async def send_message(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['message'] = message.text

    await state.finish()
    try:
        await bot.send_message(
            data['user_id'],
            text="<i>от <b>Администратора</b></i>   📨\n\n" + data['message'],
            parse_mode='HTML'
        )
        await message.answer(text="Выполнено!")
    except:
        await message.answer(
            text="Вы ввели неправильный ID пользователя! 😟\n"
                 "Попробуйте повторить отправку /message"
        )
