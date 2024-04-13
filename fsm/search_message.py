from aiogram.dispatcher.filters.state import State, StatesGroup


class SendSiteSearch(StatesGroup):
    search_islam_site = State()


class SendBrowserSearch(StatesGroup):
    search_browser = State()
