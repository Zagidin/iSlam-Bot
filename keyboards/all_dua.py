from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

all_dua = ReplyKeyboardMarkup(resize_keyboard=True)

btn1 = KeyboardButton(text='Дуа при Выходе из 🏠')
btn2 = KeyboardButton(text='Дуа при Входе 🏠')
btn3 = KeyboardButton(text='Дуа перед Едой 🍽️')
btn4 = KeyboardButton(text='Дуа после Еды 🥣')

all_dua.add(btn2)
all_dua.row(btn3, btn4)
all_dua.add(btn1)
