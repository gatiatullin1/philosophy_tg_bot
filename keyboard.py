from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton
                           )

start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/random_quote')
b4 = KeyboardButton('/random_thinker')
start_kb.add(b1, b2).add(b3, b4)
