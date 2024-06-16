import text_file
from time import sleep
from aiogram import types
from bot.registar_bot import dp
from keyboards.oplata import summa
from img_load import (
    fadjr, zuhr, asr, magrib, isha,
    vid_1, vid_2, vid_3, vid_4,
    vid_5, vid_6, vid_7, vid_8,
    vid_9, vid_10
)
from base.base_users import select_admin_users_sms
from keyboards.keyboard_surah.all_surah import all_surah
from surah_load import (
    sura_1, sura_2, sura_3, sura_4, sura_5, sura_6, sura_7,
    sura_8, sura_9, sura_10, sura_11, sura_12, sura_13,
    sura_14, sura_15, sura_16, sura_17, sura_18,
    sura_19, sura_20, sura_21, sura_22, sura_23, sura_24,
    sura_25, sura_26, sura_27, sura_28, sura_29, sura_30
)
from keyboards.keybard_dua import (
    dua_list_one, dua_list_two, dua_list_tree, dua_list_four
)
from base.setting_write_base import delete_user_base_settings


# Для Сур
text_sms = "Идёт Обработка файла ...\n\nПодождите немного :)"


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
    elif message.text == '<= Читать Суру =>':
        await message.reply(
            "Выберите Суру",
            reply_markup=all_surah
        )
    elif message.text == 'Сура ~ 1':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_1)
    elif message.text == 'Сура ~ 2':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_2)
    elif message.text == 'Сура ~ 3':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_3)
    elif message.text == 'Сура ~ 4':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_4)
    elif message.text == 'Сура ~ 5':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_5)
    elif message.text == 'Сура ~ 6':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_6)
    elif message.text == 'Сура ~ 7':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_7)
    elif message.text == 'Сура ~ 8':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_8)
    elif message.text == 'Сура ~ 9':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_9)
    elif message.text == 'Сура ~ 10':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_10)
    elif message.text == 'Сура ~ 11':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_11)
    elif message.text == 'Сура ~ 12':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_12)
    elif message.text == 'Сура ~ 13':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_13)
    elif message.text == 'Сура ~ 14':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_14)
    elif message.text == 'Сура ~ 15':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_15)
    elif message.text == 'Сура ~ 16':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_16)
    elif message.text == 'Сура ~ 17':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_17)
    elif message.text == 'Сура ~ 18':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_18)
    elif message.text == 'Сура ~ 19':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_19)
    elif message.text == 'Сура ~ 20':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_20)
    elif message.text == 'Сура ~ 21':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_21)
    elif message.text == 'Сура ~ 22':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_22)
    elif message.text == 'Сура ~ 23':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_23)
    elif message.text == 'Сура ~ 24':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_24)
    elif message.text == 'Сура ~ 25':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_25)
    elif message.text == 'Сура ~ 26':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_26)
    elif message.text == 'Сура ~ 27':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_27)
    elif message.text == 'Сура ~ 28':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_28)
    elif message.text == 'Сура ~ 29':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_29)
    elif message.text == 'Сура ~ 30':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_30)
    elif message.text == '<= Выбрать Дуа =>':
        await message.answer(
            "Выберите Дуа",
            reply_markup=dua_list_one.dua_list_one
        )
    elif message.text == '🌄 Фаджр':
        await message.answer_photo(
            vid_1,
            caption=f"Совершение первого рак'ата молитвы\n\n"
                    f"Стоя, поднимите обе руки так, чтобы кончики пальцев "
                    f"были на уровне"
                    f" плеч или ушей. Поверните ладони от себя. "
                    f"Взгляд устремлён в то место, "
                    f"которого коснётся голова в земном поклоне.\n\n"
                    f"Произнесите:\n"
                    f"\nАллаху акбар\n"
                    f" - Аллах Велик"
        )
        await message.answer_photo(
            vid_2,
            caption=f"Положите руки на грудь, правая рука поверх левой.\n\n"
                    f"Произнесите:\n"
                    f"А'узу би-Лляхи мин аш-шайтани р-раджим\n"
                    f" - Я прибегаю к Аллаху, во избежание проклятого сатаны."
                    f"\n\nПроизнести суру 'Аль-Фатиха'\n\n\nВ РАЗРАБОТКЕ!"
        )
    elif message.text in ('🏙️ Зухр', '🌇 Аср', '🌅 Магриб', '🌃 Иша'):
        await message.answer(
            text="В РАЗРАБОТКЕ!\n\nСкоро появится)"
        )
    else:
        await message.answer(
            "Выберите Дуа",
            reply_markup=dua_list_one.dua_list_one
        )
