from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


namaz = InlineKeyboardMarkup()

namaz.add(
    InlineKeyboardButton(
        text='Омовение',
        callback_data='namaz'
    )
)
