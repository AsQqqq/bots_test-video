from aiogram import types, Dispatcher
from import_bot import dp
import json, string

async def no_message(message:types.Message):
	if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
		.intersection(set(json.load(open('other/no_message.json')))) != set():
			await message.answer('данные слова запрещены. Вырожайтесь правильно')
			await message.delete()
	else:
		await message.answer('Я не понимаю твои слова. Напиши /start или /help')

async def download_game(message: types.Message):
	await message.answer('скачивание игры...')
	await message.delete()

def reg_handler(dp:Dispatcher):
	dp.register_message_handler(download_game, text='скачать игру')
	dp.register_message_handler(no_message)