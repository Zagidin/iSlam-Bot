from time import sleep
from bot.registar_bot import dp
from keyboards.oplata import pay_bot
from img_load import (
    shag_1, shag_2, shag_3, shag_4,
    shag_5, shag_6, shag_7, shag_8,
    shag_9
)
from aiogram.types import ReplyKeyboardRemove
from keyboards.keyboard_namaz.namaz_key import namaz


@dp.callback_query_handler()
async def callback_send_bot(callback):
    if callback.data == 'proect_help':

        await callback.message.answer(
            f"iSlam Dua - полезный Исламский бот, "
            f"в котором, Вы можете просмореть разные Дуа ( Молитвы ).\n"
            f"С помощью этого бота, Вам не придётся искать нужное Дуа на прасторах Интернета.\n\n"
            f"Вы можете помочь проекту, сделав добровольное пожертвование.",
            reply_markup=pay_bot
        )
    elif callback.data == 'namaz':

        await callback.message.answer_photo(
            shag_1,
            caption='Перед Омовением произнесите:\n\n'
                    'ﺑِﺴْﻢِ ٱﻟﻠّٰﻪِ'
                    '\nБисми Лляхи\n - Во имя Аллаха',
            reply_markup=ReplyKeyboardRemove()
        )

        sleep(1.5)

        await callback.message.answer_photo(
            shag_2,
            caption='Промыть руки 3 раза вместе.\n'
                    'Включая запястья и пространство между пальцами рук.'
        )

        sleep(1.5)

        await callback.message.answer_photo(
            shag_3,
            caption='Прополоскать рот 3 раза.\n'
                    'Наполнить правую ладонь, набрать воду в рот, '
                    'сделать полоскание и выплюнуть.'
        )

        sleep(2)

        await callback.message.answer_photo(
            shag_4,
            caption='Прочистить нос 3 раза.\n'
                    'Наполнить правую ладонь, хорошо втянуть воду носом, а '
                    'затем высморкаться левой рукой.'
        )

        sleep(1.5)

        await callback.message.answer_photo(
            shag_5,
            caption='Помыть лицо от границы волос над лбом, до подбородка, '
                    'а также от уха до уха. Вода должна попасть на всю отмеченную область. '
                    'Данную процедуру можно делать как 1, так и 3 раза.\n'
                    '(Если у Вас есть борода, нужно набрать воду и промыть ей подбородок, '
                    'а затем прочесать бороду мокрыми пальцами от начала до конца).'
        )

        sleep(1.5)

        await callback.message.answer_photo(
            shag_6,
            caption='Помыть руки от кончиков пальцев до локтя 3 раза, начиная с правой.'
        )

        sleep(1.5)

        await callback.message.answer_photo(
            shag_7,
            caption='Провести мокрыми руками от границы волос головы до затылочной области '
                    'и обратно одним движением, протирая ее.'
        )

        sleep(1.5)

        await callback.message.answer_photo(
            shag_8,
            caption='Протереть внутреннюю поверхность ушей влажными указательными пальцами 1 раз, '
                    'а большими пальцами - заднюю поверхность ушей;\n'
                    'Оба уха протираются одновременно.'
        )

        sleep(1.5)

        await callback.message.answer_photo(
            shag_9,
            caption='Трижды моет ноги до щиколоток включительно, начиная с правой ноги. '
                    'Нужно также промывать промежутки между пальцами.',
            reply_markup=namaz
        )
