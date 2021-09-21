from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# перший варіант меню
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("1")],
        [KeyboardButton("2"), KeyboardButton("3")],
    ],
    resize_keyboard=True)

#другий варіант меню
val1 = KeyboardButton("1")
val2 = KeyboardButton("2")
val3 = KeyboardButton("3")
menu1 = ReplyKeyboardMarkup(resize_keyboard=True).add(val1, val2, val3)