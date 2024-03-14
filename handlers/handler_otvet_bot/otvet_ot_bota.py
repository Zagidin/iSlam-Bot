import text_file

from aiogram import types
from bot.registar_bot import dp
from keyboards.all_dua import all_dua
from keyboards.oplata import summa


@dp.message_handler(lambda message: types.Message)
async def otvet(message: types.Message):
    if message.text == 'Ва-алейкум ас-саля́м ва-рахмату-Лла́хи ва-барака́тух 👋':
        await message.answer(
            "Выбери Дуа",
            reply_markup=all_dua
        )
    elif message.text == 'Дуа при Входе 🏠':
        file = open('ALL_DUA/Entrance_home.pdf', 'rb')
        await message.answer_document(file)
        await message.answer(
            text_file.entrance_home,
            parse_mode='HTML'
        )
    elif message.text == 'Дуа перед Едой 🍽️':
        file = open('ALL_DUA/Before_Eating.pdf', 'rb')
        await message.answer_document(file)
        await message.answer(
            text_file.before_eating,
            parse_mode='HTML'
        )
    elif message.text == 'Дуа после Еды 🥣':
        file = open('ALL_DUA/After_Eating.pdf', 'rb')
        await message.answer_document(file)
        await message.answer(
            text_file.after_eating,
            parse_mode='HTML'
        )
    elif message.text == 'Дуа при Выходе из 🏠':
        file = open('ALL_DUA/Exit_home.pdf', 'rb')
        await message.answer_document(file)
        await message.answer(
            text_file.exit_home,
            parse_mode='HTML'
        )
    elif message.text in summa:
        await message.answer("Пока в Разработке!", reply_markup=all_dua)
    else:
        await message.answer("Выберите Дуа", reply_markup=all_dua)