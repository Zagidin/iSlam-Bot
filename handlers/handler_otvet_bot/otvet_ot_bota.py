import text_file

from aiogram import types
from bot.registar_bot import dp
from keyboards.keybard_dua import (
    dua_list_one, dua_list_two, dua_list_tree
)
from keyboards.oplata import summa


@dp.message_handler(lambda message: types.Message)
async def otvet(message: types.Message):
    if message.text == 'Ва-алейкум ас-саля́м ва-рахмату-Лла́хи ва-барака́тух 👋':
        await message.answer(
            "Выбери Дуа",
            reply_markup=dua_list_one.dua_list_one
        )
    elif message.text == 'Далее => 📖📚':
        await message.reply(
            "Выберите Дуа",
            reply_markup=dua_list_two.dua_list_two
        )
    elif message.text == 'Далее => 📖 📚':
        await message.reply(
            "Выберите Дуа",
            reply_markup=dua_list_tree.dua_list_tree
        )
    elif message.text == '📚📖 <= Назад':
        await message.reply(
            "Выберите Дуа",
            reply_markup=dua_list_one.dua_list_one
        )
    elif message.text == '📚 📖 <= Назад':
        await message.reply(
            "Выберите Дуа",
            reply_markup=dua_list_two.dua_list_two
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
    elif message.text == 'Дуа перед сном 🛌':
        await message.answer(
            text_file.pered_snom,
            parse_mode='HTML'
        )
    elif message.text in summa:
        await message.answer(
            "Пока в Разработке!",
            reply_markup=dua_list_one.dua_list_one
        )
    elif message.text == 'Сура ~ 1':
        file = open('SURAH/RU~01.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 2':
        file = open('SURAH/RU~02.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 3':
        file = open('SURAH/RU~03.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 4':
        file = open('SURAH/RU~04.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 5':
        file = open('SURAH/RU~05.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 6':
        file = open('SURAH/RU~06.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 7':
        file = open('SURAH/RU~07.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 8':
        file = open('SURAH/RU~08.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 9':
        file = open('SURAH/RU~09.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 10':
        file = open('SURAH/RU~10.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 11':
        file = open('SURAH/RU~11.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 12':
        file = open('SURAH/RU~12.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 13':
        file = open('SURAH/RU~13.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 14':
        file = open('SURAH/RU~14.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 15':
        file = open('SURAH/RU~15.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 16':
        file = open('SURAH/RU~16.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 17':
        file = open('SURAH/RU~17.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 18':
        file = open('SURAH/RU~18.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 19':
        file = open('SURAH/RU~19.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 20':
        file = open('SURAH/RU~20.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 21':
        file = open('SURAH/RU~21.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 22':
        file = open('SURAH/RU~22.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 23':
        file = open('SURAH/RU~23.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 24':
        file = open('SURAH/RU~24.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 25':
        file = open('SURAH/RU~25.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 26':
        file = open('SURAH/RU~26.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 27':
        file = open('SURAH/RU~27.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 28':
        file = open('SURAH/RU~28.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 29':
        file = open('SURAH/RU~29.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    elif message.text == 'Сура ~ 30':
        file = open('SURAH/RU~30.pdf', 'rb')
        await message.answer("⌛")
        await message.answer("Идёт Обработка файла ...")
        await message.answer_document(file)
    else:
        await message.answer(
            "Выберите Дуа",
            reply_markup=dua_list_one.dua_list_one
        )