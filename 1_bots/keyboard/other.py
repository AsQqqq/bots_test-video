from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

#кнопки
download = KeyboardButton('скачать игру')
admin = KeyboardButton('связь с админом')

#клавиатура
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)

#регистрация
main_kb.add(download).insert(admin)