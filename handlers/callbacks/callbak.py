from bot.registar_bot import dp
from keyboards.oplata import oplata


@dp.callback_query_handler()
async def callback_send_user(callback):
    if callback.data == 'proect_help':

        await callback.message.answer(
            f"iSlam Dua - полезный Исламский бот, "
            f"который не содержит рекламы.\n\n"
            f"Вы можете помочь проекту, сделав добровольное пожертвование.",
            reply_markup=oplata
        )
