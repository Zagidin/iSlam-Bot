from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone = ReplyKeyboardMarkup(resize_keyboard=True)
phone.add(
    KeyboardButton(
        text='Поделиться номером телефона',
        request_contact=True
    )
)
