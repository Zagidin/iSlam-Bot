from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

dua_list_four = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(text='Во Время Азана 🕌🔊')
btn2 = KeyboardButton(text='В Разработке(~)')
btn3 = KeyboardButton(text='В Разработке(~)')
btn4 = KeyboardButton(text='Дуа После Азана 🕌🔇')
btn5 = KeyboardButton(text='.📚 📖 <= Назад')

dua_list_four.add(btn1)
dua_list_four.row(btn2, btn3)
dua_list_four.add(btn4)
dua_list_four.row(btn5)
