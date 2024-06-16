from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


namaz = ReplyKeyboardMarkup(resize_keyboard=True)

namaz.add(
    KeyboardButton(
        text='🌄 Фаджр'
    )
)

namaz.add(
    KeyboardButton(
        text='🏙️ Зухр'
    )
)

namaz.add(
    KeyboardButton(
        text='🌇 Аср'
    )
)

namaz.add(
    KeyboardButton(
        text='🌅 Магриб'
    )
)

namaz.add(
    KeyboardButton(
        text='🌃 Иша'
    )
)
