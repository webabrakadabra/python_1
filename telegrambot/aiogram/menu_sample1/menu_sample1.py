from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor

menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="1")],
    [KeyboardButton(text="2"), KeyboardButton(text="3")],
    [KeyboardButton(text="4"), KeyboardButton(text="5"), KeyboardButton(text="6")]
], resize_keyboard=True)

bot = Bot(token="1954554245:AAHIGTq-4P_O6fnh9tgA-BJ--wtBkV5q2Cw")  # http://t.me/tezw_ripeeew_bot
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def mess(message):
    await message.answer("Меню", reply_markup=menu)

executor.start_polling(dp)

