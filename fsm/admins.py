from aiogram.dispatcher.filters.state import State, StatesGroup


class Admins(StatesGroup):
    admin_password = State()
