from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

proect_help = InlineKeyboardMarkup()
proect_help.add(
    InlineKeyboardButton(
        text="🕌 Поддержать Проект 🏭",
        callback_data="proect_help"
    )
)
