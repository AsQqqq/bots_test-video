import config
from import_bot import dp
from aiogram.utils import executor
from handler import user, other

#1
user.reg_handler(dp)

#end
other.reg_handler(dp)

async def on_startup(_):
	pass

if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True, on_startup=on_startup)