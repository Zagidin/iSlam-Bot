from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

summa = ["50 ₽", "100 ₽", "150 ₽"]

pay_bot = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton('50 ₽')
btn2 = KeyboardButton('100 ₽')
btn3 = KeyboardButton('150 ₽')
pay_bot.row(btn1, btn2)
pay_bot.add(btn3)