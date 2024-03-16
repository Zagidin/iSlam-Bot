from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


dua_list_two = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(text='Дуа перед сном 🛌')
btn2 = KeyboardButton(text='Дуа при надевании одежды 👔')
btn3 = KeyboardButton(text='При надевании в новую одежду 👔')
btn4 = KeyboardButton(text='Дуа после сна 🌅🛏️')
btn5 = KeyboardButton(text='📚📖 <= Назад')
btn6 = KeyboardButton(text='Далее => 📖 📚')

dua_list_two.add(btn2)
dua_list_two.row(btn1, btn4)
dua_list_two.add(btn3)
dua_list_two.add(btn5, btn6)
