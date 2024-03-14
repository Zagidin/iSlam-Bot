from bot.registar_bot import dp
from keyboards.oplata import pay_bot


@dp.callback_query_handler()
async def callback_send_bot(callback):
    if callback.data == 'proect_help':

        await callback.message.answer(
            f"iSlam Dua - полезный Исламский бот, "
            f"который не содержит рекламы.\n\n"
            f"Вы можете помочь проекту, сделав добровольное пожертвование.",
            reply_markup=pay_bot
        )
