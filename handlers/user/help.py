from bot.registar_bot import dp
from aiogram import types
from inlanekey.helpproect import proect_help


@dp.message_handler(commands=['help'])
async def help_bot(message: types.Message):
    await message.answer(
        f"Дуа — это личная мольба мусульманина на родном языке, обращение к Аллаху "
        f"в исламе. Одна из разновидностей поклонения.\nДуа произносят в различных "
        f"житейских ситуациях. Обычно мусульмане просят Аллаха о помощи, начиная "
        f"какое-то дело.\n\n<b>При чтении дуа мусульмане обращаются в сторону Мекки (киблы), "
        f"поднимают руки на уровне плеч ладонями вверх и пониженным голосом произносят "
        f"мольбы на арабском или другом, понятном обращающемуся языке.</b>\n\n\n"
        f"1) <u><b>Читать Сура</b> - /surah</u>\n\n"
        f"2) <u><b>Слушать Нашиды</b> - /nasheed</u>\n\n"
        f"3) <u><b>Обучение Намазу</b> - /namaz</u>",
        parse_mode='HTML',
        reply_markup=proect_help
    )

