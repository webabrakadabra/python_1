from aiogram import Bot, Dispatcher, executor, types
from config import token_telegram
from murkup import menu

bot = Bot(token_telegram)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message):
    await message.answer("Привіт Людино " + message.from_user.first_name + " " + message.from_user.last_name +
                         "! Я бот Корявко.")


@dp.message_handler(commands=['help'])
async def help_command(message):
    await message.answer("Привіт Людино " + message.from_user.first_name + " " + message.from_user.last_name +
                         ". Як я тобі можу допомогти???.")
    # await message.reply(message.text)
    # await message.send_message(message.from_user.id, message.text)


@dp.message_handler(commands=['menu'])
async def echo_message(message):
    await bot.send_message(message.from_user.id, "Меню", reply_markup=menu)


@dp.message_handler(text="1")
async def one(message):
    await message.answer("OOOOOdin")

if __name__ == "__main__":
    executor.start_polling(dp)
