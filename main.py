from bot.registar_bot import dp
from bot.start_bot import starts_bot
from aiogram import types
from keyboards.otvet_bot import otvet_botu
from keyboards.all_dua import all_dua


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        f"<b>Ас-саляму алейкум "
        f"ва-рахмату-Лла́хи ва-барака́тух @{message.from_user.username}🤚</b>",
        parse_mode='HTML',
        reply_markup=otvet_botu
    )


@dp.message_handler(lambda message: types.Message)
async def otvet(message: types.Message):
    if message.text == 'Ва-алейкум ас-саля́м ва-рахмату-Лла́хи ва-барака́тух 👋':
        await message.answer(
            "Выбери Дуа",
            reply_markup=all_dua
        )
    elif message.text == 'Дуа при Входе 🏠':
        file = open('ALL_DUA/.pdf', 'rb')
        await message.answer_document(file)
    elif message.text == 'Дуа перед Едой 🍽️':
        file = open('ALL_DUA/Before_Eating.pdf', 'rb')
        await message.answer_document(file)
    elif message.text == 'Дуа после Еды 🥣':
        file = open('ALL_DUA/.pdf', 'rb')
        await message.answer_document(file)
    elif message.text == 'Дуа при Выходе из 🏠':
        file = open('ALL_DUA/Exit_home.pdf', 'rb')
        await message.answer_document(file)
    else:
        await message.answer("Выберите Дуа", reply_markup=all_dua)


if __name__ == "__main__":
    starts_bot()
