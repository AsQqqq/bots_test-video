from aiogram import types, Dispatcher
import config
from import_bot import dp
from keyboard import main_kb

ID = config.ADMIN

async def start_command(message: types.Message):
	if message.from_user.id == ID:
		await message.answer('привет админ', reply_markup=main_kb)
	else:
		await message.answer('привет пользователь', reply_markup=main_kb)

def reg_handler(dp:Dispatcher):
	dp.register_message_handler(start_command, commands=['start', 'help'])