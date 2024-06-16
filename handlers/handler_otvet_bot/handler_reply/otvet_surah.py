from aiogram import types
from .otvet_namaz import dp
from keyboards.keybard_dua import dua_list_one
from surah_load import (
    sura_1, sura_2, sura_3, sura_4, sura_5, sura_6, sura_7,
    sura_8, sura_9, sura_10, sura_11, sura_12, sura_13,
    sura_14, sura_15, sura_16, sura_17, sura_18,
    sura_19, sura_20, sura_21, sura_22, sura_23, sura_24,
    sura_25, sura_26, sura_27, sura_28, sura_29, sura_30
)


text_sms = "Идёт Обработка файла ...\n\nПодождите немного :)"


@dp.message_handler(lambda message: types.Message)
async def otvet_surah(message: types):
    if message.text == 'Сура ~ 1':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_1)
    elif message.text == 'Сура ~ 2':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_2)
    elif message.text == 'Сура ~ 3':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_3)
    elif message.text == 'Сура ~ 4':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_4)
    elif message.text == 'Сура ~ 5':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_5)
    elif message.text == 'Сура ~ 6':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_6)
    elif message.text == 'Сура ~ 7':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_7)
    elif message.text == 'Сура ~ 8':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_8)
    elif message.text == 'Сура ~ 9':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_9)
    elif message.text == 'Сура ~ 10':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_10)
    elif message.text == 'Сура ~ 11':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_11)
    elif message.text == 'Сура ~ 12':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_12)
    elif message.text == 'Сура ~ 13':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_13)
    elif message.text == 'Сура ~ 14':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_14)
    elif message.text == 'Сура ~ 15':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_15)
    elif message.text == 'Сура ~ 16':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_16)
    elif message.text == 'Сура ~ 17':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_17)
    elif message.text == 'Сура ~ 18':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_18)
    elif message.text == 'Сура ~ 19':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_19)
    elif message.text == 'Сура ~ 20':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_20)
    elif message.text == 'Сура ~ 21':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_21)
    elif message.text == 'Сура ~ 22':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_22)
    elif message.text == 'Сура ~ 23':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_23)
    elif message.text == 'Сура ~ 24':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_24)
    elif message.text == 'Сура ~ 25':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_25)
    elif message.text == 'Сура ~ 26':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_26)
    elif message.text == 'Сура ~ 27':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_27)
    elif message.text == 'Сура ~ 28':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_28)
    elif message.text == 'Сура ~ 29':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_29)
    elif message.text == 'Сура ~ 30':
        await message.answer("⌛")
        await message.answer(text_sms)
        await message.answer_document(sura_30)
    elif message.text == '<= Выбрать Дуа =>':
        await message.answer(
            "Выберите Дуа",
            reply_markup=dua_list_one.dua_list_one
        )
    else:
        await message.answer(
            "Выберите Дуа",
            reply_markup=dua_list_one.dua_list_one
        )
