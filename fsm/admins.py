from aiogram.dispatcher.filters.state import State, StatesGroup


class Admins(StatesGroup):
    admin_password = State()


class DeleteUsers(StatesGroup):
    delete_user_num = State()
