import config
from aiogram import types, Bot
from aiogram.dispatcher import Dispatcher

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)