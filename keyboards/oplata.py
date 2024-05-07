from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

summa = ["50 ₽", "100 ₽", "150 ₽"]

pay_bot = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(summa[0])
btn2 = KeyboardButton(summa[1])
btn3 = KeyboardButton(summa[2])
pay_bot.row(btn1, btn2)
pay_bot.add(btn3)
