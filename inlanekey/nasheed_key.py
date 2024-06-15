from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)


nasheed_btn = InlineKeyboardMarkup()

nasheed_btn.add(
    InlineKeyboardButton(
        text='🎧 Слушать Нашиды 🎧',
        web_app=WebAppInfo(
            url="https://hithub.cc/search/нашиды+2022г"
        )
    )
)
