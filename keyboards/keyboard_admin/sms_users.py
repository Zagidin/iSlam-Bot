from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


smsusers = ReplyKeyboardMarkup(resize_keyboard=True)
smsusers.add(
    KeyboardButton(
        text='Посмореть Сообщения от Пользователей'
    )
)
