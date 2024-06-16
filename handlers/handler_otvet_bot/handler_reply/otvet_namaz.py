from bot.registar_bot import dp
from aiogram import types
from img_load import (
    fadjr, zuhr, asr, magrib, isha,
    vid_1, vid_2, vid_3, vid_4,
    vid_5, vid_6, vid_7, vid_8,
    vid_9, vid_10
)


@dp.message_handler(lambda message: types.Message)
async def otvet_namaz(message: types.Message):
    if message.text == '🌄 Фаджр':
        await message.answer_photo(
            vid_1,
            caption=f"Стоя, поднимите обе руки так, чтобы кончики пальцев были на уровне"
                    f" плеч или ушей. Поверните ладони от себя. Взгляд устремлён в то место, "
                    f"которого коснётся голова в земном поклоне.\n\n"
                    f"Произнесите:\n"
                    f"\nАллаху акбар\n"
                    f" - Аллах Велик"
        )