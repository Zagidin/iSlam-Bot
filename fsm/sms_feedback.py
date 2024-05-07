from aiogram.dispatcher.filters.state import State, StatesGroup


class Userfeedback(StatesGroup):
    sms_feedback = State()
    phone = State()
