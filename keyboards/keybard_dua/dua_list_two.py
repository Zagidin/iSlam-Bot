from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


dua_list_two = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(text='Дуа перед сном 🛌')
btn2 = KeyboardButton(text='В Разработке (~)')
btn3 = KeyboardButton(text='В Разработке (~)')
btn4 = KeyboardButton(text='В Разработке (~)')
btn5 = KeyboardButton(text='📚📖 <= Назад')
btn6 = KeyboardButton(text='Далее => 📖 📚')

dua_list_two.add(btn1)
dua_list_two.row(btn2, btn3)
dua_list_two.add(btn4)
dua_list_two.add(btn5, btn6)
