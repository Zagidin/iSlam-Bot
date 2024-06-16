import text_file
from aiogram import types
from bot.registar_bot import dp
from keyboards.oplata import summa
from keyboards.keyboard_surah.all_surah import all_surah
from keyboards.keybard_dua import (
    dua_list_one, dua_list_two, dua_list_tree, dua_list_four
)


@dp.message_handler(lambda message: types.Message)
async def otvet_dua(message: types.Message):
    if message.text == 'Далее => 📖📚':
        await message.reply(
            "Выберите Дуа",
            reply_markup=dua_list_two.dua_list_two
        )
    elif message.text == 'Далее => 📖 📚':
        await message.reply(
            "Выберите Дуа",
            reply_markup=dua_list_tree.dua_list_tree
        )
    elif message.text == 'Далее => 📖 📚.':
        await message.reply(
            "Выберите Дуа",
            reply_markup=dua_list_four.dua_list_four
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
    elif message.text == '.📚 📖 <= Назад':
        await message.reply(
            "Выберите Дуа",
            reply_markup=dua_list_tree.dua_list_tree
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
            text_file.before_sleep,
            parse_mode='HTML'
        )
    elif message.text == 'Дуа после сна 🌅🛏️':
        await message.answer(text_file.after_sleep, parse_mode='HTML')
    elif message.text in summa:
        await message.answer(
            "Пока в Разработке!",
            reply_markup=dua_list_one.dua_list_one
        )
    elif message.text == 'Дуа при надевании одежды 👔':
        await message.answer(
            text_file.clothe_clothes,
            parse_mode='HTML'
        )
    elif message.text == 'При надевании в новую одежду 👔':
        await message.answer(
            text_file.new_clothe_clothes,
            parse_mode='HTML'
        )
    elif message.text == 'Дуа до Омовения 🚰':
        await message.answer(
            text_file.before_ablution,
            parse_mode='HTML'
        )
    elif message.text == 'Дуа после Омовения 🚰':
        await message.answer(
            text_file.after_ablution,
            parse_mode='HTML'
        )
    elif message.text == 'Дуа при Выходе из 🚾🚽':
        await message.answer(
            text_file.after_toilet,
            parse_mode='HTML'
        )
    elif message.text == 'Дуа при Входе в 🚾🚽':
        await message.answer(
            text_file.before_toilet,
            parse_mode='HTML'
        )
    elif message.text == 'Во Время Азана 🕌🔊':
        await message.answer(
            text_file.before_az1an,
            parse_mode='HTML'
        )
    elif message.text == 'Дуа После Азана 🕌🔇':
        await message.answer(
            text_file.after_az1an,
            parse_mode='HTML'
        )
    elif message.text == '<= Читать Суру =>':
        await message.reply(
            "Выберите Суру",
            reply_markup=all_surah
        )
    else:
        await message.answer(
            "Выберите Дуа",
            reply_markup=dua_list_one.dua_list_one
        )
