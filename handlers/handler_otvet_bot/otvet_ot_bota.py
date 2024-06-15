import text_file

from time import sleep
from aiogram import types
from bot.registar_bot import dp
from img_load import (
    fadjr, zuhr, asr, magrib, isha
)
from keyboards.keybard_dua import (
    dua_list_one, dua_list_two, dua_list_tree, dua_list_four
)
from keyboards.oplata import summa
from keyboards.keyboard_surah.all_surah import all_surah
from base.base_users import select_admin_users_sms
from base.setting_write_base import delete_user_base_settings


@dp.message_handler(lambda message: types.Message)
async def bot_send_message(message: types.Message):
    if message.text == 'Ва-алейкум ас-саля́м ва-рахмату-Лла́хи ва-барака́тух 👋':
        await message.answer(
            "Выбери Дуа",
            reply_markup=dua_list_one.dua_list_one
        )
    elif message.text == 'Посмореть Сообщения от Пользователей':

        if select_admin_users_sms():
            await message.answer(text="Пользователи ждущие Вашего ответа ...")
            await message.answer("⏳")
            sleep(1)
            for el in select_admin_users_sms():
                await message.answer(
                    text="Пользователь: <b>№ {}</b>\n"
                         "\nТелеграм 💬\n<b>{}</b>\n"
                         "\nНомер телефона 📲\n<code>{}</code>\n"
                         "\n<u><i><b>User-ID:</b></i></u> <code>{}</code>\n"
                         "\nСообщение 📝\n**************\n"
                         "<b><i>{}</i></b>\n"
                         "\n************\n\n\n<b><i>Ответить пользователю 💬</i></b>\n"
                         "/message".format(el[0], el[1], el[2], el[3], el[4]),
                    parse_mode='HTML'
                )
        else:
            await message.delete()
            await message.answer(text="Сообщений от пользователей нет! :)")
    elif message.text == 'Очистить SMS-Пользователей':

        delete_user_base_settings()

        await message.answer(
            text="Выполнено! 🗑"
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
    elif message.text == '🌄 Фаджр':
        await message.answer_photo(
            fadjr,
            caption='Фаджр - 2 ракаата',
            parse_mode='HTML'
        )
        await message.answer(

        )
    elif message.text == '🏙️ Зухр':
        await message.answer(
            text='В разработке'
        )
    elif message.text == '🌇 Аср':
        await message.answer(
            text='В разработке'
        )
    elif message.text == '🌅 Магриб':
        await message.answer(
            text='В разработке'
        )
    elif message.text == '🌃 Иша':
        await message.answer(
            text='В разработке'
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
