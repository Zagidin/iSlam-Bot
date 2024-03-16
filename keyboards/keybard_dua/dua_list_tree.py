from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

dua_list_tree = ReplyKeyboardMarkup(resize_keyboard=True)

btn1 = KeyboardButton(text='Дуа при Выходе из 🚾🚽')
btn2 = KeyboardButton(text='Дуа до Омовения 🚰')
btn3 = KeyboardButton(text='Дуа при Входе в 🚾🚽')
btn4 = KeyboardButton(text='Дуа после Омовения 🚰')
btn5 = KeyboardButton(text='📚 📖 <= Назад')
btn6 = KeyboardButton(text='Далее => 📖 📚.')

dua_list_tree.add(btn1)
dua_list_tree.row(btn2, btn3)
dua_list_tree.add(btn4)
dua_list_tree.add(btn5, btn6)
