from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

summa = ["50 ₽", "100 ₽", "150 ₽"]

oplata = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton('50 ₽')
btn2 = KeyboardButton('100 ₽')
btn3 = KeyboardButton('150 ₽')
oplata.row(btn1, btn2)
oplata.add(btn3)
