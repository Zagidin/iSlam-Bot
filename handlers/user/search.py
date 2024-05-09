from bot.registar_bot import dp
from aiogram import types
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)
from aiogram.dispatcher import FSMContext
from fsm.search_message import SendSiteSearch


@dp.message_handler(commands=['search'])
async def search_message(message: types.Message):
    await message.answer(
        text="<i>Поиск на сайте <b>Islam.global</b></i>\n\nЧто хотите найти?",
        parse_mode='HTML'
    )

    await SendSiteSearch.search_islam_site.set()


@dp.message_handler(state=SendSiteSearch.search_islam_site)
async def search_message(message: types.Message, state: FSMContext) -> None:

    async with state.proxy() as data:
        data['search_islam_site'] = message.text.lower()

    await state.finish()

    url_search = "https://islam.global/search/?_token=wdXCbHI9XPga80Fh6aCsLSBTo66d9kNm0FFqsE1B&query=" + data[
        'search_islam_site'
    ]

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            text="ПОКАЗАТЬ 🔎",
            web_app=WebAppInfo(
                url=url_search
            )
        )
    )

    await message.answer(
        text="Ответ обработан\nнажмите на кнопку ниже.\n\nЧтобы создать запрос заново\nНажмите на /search.",
        reply_markup=markup
    )
