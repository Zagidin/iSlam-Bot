from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_users = ReplyKeyboardMarkup(resize_keyboard=True)
admin_users.add(
    KeyboardButton(
        text='Посмореть Сообщения от Пользователей'
    )
)
admin_users.add(
    KeyboardButton(
        text="Очистить SMS-Пользователей"
    )
)
