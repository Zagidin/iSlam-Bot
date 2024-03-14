from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

dua_list_tree = ReplyKeyboardMarkup(resize_keyboard=True)

btn1 = KeyboardButton(text='В Разработке (~1)')
btn2 = KeyboardButton(text='В Разработке (~2)')
btn3 = KeyboardButton(text='В Разработке (~3)')
btn4 = KeyboardButton(text='В Разработке (~4)')
btn5 = KeyboardButton(text='📚 📖 <= Назад')

dua_list_tree.add(btn1)
dua_list_tree.row(btn2, btn3)
dua_list_tree.add(btn4)
dua_list_tree.add(btn5)
