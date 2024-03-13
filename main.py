import text_file

from bot.registar_bot import dp
from bot.start_bot import starts_bot
from aiogram import types
from keyboards.otvet_bot import otvet_botu
from keyboards.all_dua import all_dua
from keyboards.oplata import oplata
from inlanekey.helpproect import proect_help


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        f"<b>Ас-саляму алейкум "
        f"ва-рахмату-Лла́хи ва-барака́тух @{message.from_user.username}🤚</b>",
        parse_mode='HTML',
        reply_markup=otvet_botu
    )


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(
        f"Дуа — это личная мольба мусульманина на родном языке, обращение к Аллаху "
        f"в исламе. Одна из разновидностей поклонения.\nДуа произносят в различных "
        f"житейских ситуациях. Обычно мусульмане просят Аллаха о помощи, начиная "
        f"какое-то дело.\n\n<b>При чтении дуа мусульмане обращаются в сторону Мекки (киблы), "
        f"поднимают руки на уровне плеч ладонями вверх и пониженным голосом произносят "
        f"мольбы на арабском или другом, понятном обращающемуся языке.</b>\n\n",
        parse_mode='HTML',
        reply_markup=proect_help
    )


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
    elif message.text == "50 ₽" or message.text == "100 ₽" or message.text == "150 ₽":
        await message.answer("Пока в Разработке!", reply_markup=all_dua)
    else:
        await message.answer("Выберите Дуа", reply_markup=all_dua)


@dp.callback_query_handler()
async def callback_send_user(callback):
    if callback.data == 'proect_help':

        await callback.message.answer(
            f"iSlam Dua - полезный Исламский бот, "
            f"который не содержит рекламы.\n\n"
            f"Вы можете помочь проекту, сделав добровольное пожертвование.",
            reply_markup=oplata
        )

if __name__ == "__main__":
    starts_bot()
