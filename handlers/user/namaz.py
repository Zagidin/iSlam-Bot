from bot.registar_bot import dp
from aiogram.types import Message
from inlanekey import namaz_key


@dp.message_handler(commands=['namaz'])
async def namaz(message: Message):
    await message.answer(
        text=f"<b>Обучение Намазу</b>",
        parse_mode='HTML'
    )
    await message.answer(
        text=f"Каждый Мусульманин <u><i>обязан совершать ежедневный пятикратный намаз.</i></u>\n\n"
             f"Обязанность читать намаз распространяется <i>на всех мусульман</i>, независимо "
             f"от их положения в обществе или материального положения.\n\n"
             f"Определенные послабления допускаются лишь в тех случаях, когда читать "
             f"намаз <u><i>не позволяет здоровье.</i></u>",
        parse_mode='HTML'
    )
    await message.answer(
        text=f"Перед тем как читать намаз нужно всегда делать Омовение 💧",
        reply_markup=namaz_key.namaz
    )
