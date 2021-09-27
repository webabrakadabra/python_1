from aiogram import Bot, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("1"), KeyboardButton("2"), KeyboardButton("3"),
                                                     KeyboardButton("4"), KeyboardButton("5"), KeyboardButton("6"))

bot = Bot(token="1954554245:AAHIGTq-4P_O6fnh9tgA-BJ--wtBkV5q2Cw")  # http://t.me/tezw_ripeeew_bot
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def fun(message):
    await message.answer("TEXT", reply_markup=menu)

executor.start_polling(dp)