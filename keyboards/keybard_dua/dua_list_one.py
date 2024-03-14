from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

dua_list_one = ReplyKeyboardMarkup(resize_keyboard=True)

btn1 = KeyboardButton(text='Дуа при Выходе из 🏠')
btn2 = KeyboardButton(text='Дуа при Входе 🏠')
btn3 = KeyboardButton(text='Дуа перед Едой 🍽️')
btn4 = KeyboardButton(text='Дуа после Еды 🥣')
btn5 = KeyboardButton(text='Далее => 📖📚')
btn6 = KeyboardButton(text='<= Читать Суру =>')

dua_list_one.add(btn2)
dua_list_one.row(btn3, btn4)
dua_list_one.add(btn1)
dua_list_one.add(btn5)
dua_list_one.add(btn6)
