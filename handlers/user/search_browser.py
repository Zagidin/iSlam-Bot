from bot.registar_bot import dp
from aiogram import types
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)
from aiogram.dispatcher import FSMContext
from fsm.search_message import SendBrowserSearch


@dp.message_handler(commands=['search_browser'])
async def search_browser(message: types.Message):
    await message.answer(
        text="<i>Поиск в <b>Яндекс</b></i>\n\nЧто хотите найти?",
        parse_mode='HTML'
    )

    await SendBrowserSearch.search_browser.set()


@dp.message_handler(state=SendBrowserSearch.search_browser)
async def search_browser(message: types, state: FSMContext) -> None:

    async with state.proxy() as data:
        data['search_browser'] = message.text.lower()

    await state.finish()

    url_search_browser = "https://yandex.ru/search/?text=" + data['search_browser']

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            text="ПОКАЗАТЬ 🔎",
            web_app=WebAppInfo(
                url=url_search_browser
            )
        )
    )

    await message.answer(
        text=f"Ответ обработан\nнажмите на кнопку ниже."
             f"\n\nЧтобы создать запрос заново\nНажмите на /search_browser",
        reply_markup=markup
    )
