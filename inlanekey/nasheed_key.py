from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo


nasheed_btn = InlineKeyboardMarkup()
nasheed_btn.add(
    InlineKeyboardButton(
        text='(1) Слушать Нашиды',
        web_app=WebAppInfo(
            url="https://zvu4no.org/tracks/самый%20красивый%20нашид"
        )
    )
)
nasheed_btn.add(
    InlineKeyboardButton(
        text='(2) Слушать Нашиды',
        web_app=WebAppInfo(
            url="https://muzvibe.org/search/САМЫЙ%20Красивый%20Нашид"
        )
    )
)
nasheed_btn.add(
    InlineKeyboardButton(
        text='(3) Слушать Нашиды',
        web_app=WebAppInfo(
            url="https://azan.ru/audio/view/nashidyi-bez-muzyiki-28"
        )
    )
)
nasheed_btn.add(
    InlineKeyboardButton(
        text='(4) Слушать Нашиды',
        web_app=WebAppInfo(
            url="https://hithub.cc/search/нашиды+2022г"
        )
    )
)
