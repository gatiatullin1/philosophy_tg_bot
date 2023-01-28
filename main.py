from aiogram import Bot, Dispatcher, executor, types

from config import TOKKEN_API, RANDOM_QUOTE_STICKER_ID
from commands import commands
from thinkers import (thinkers,
                      text_about_thinker,
                      thinker_location,
                      inline_keyboard)
from keyboard import start_kb

from random import randrange

bot = Bot(TOKKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот успешно запущен!')


@dp.message_handler(commands=['start', 'help', 'description'])
async def major_commands(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=commands[message.text],
                           parse_mode='HTML',
                           reply_markup=start_kb
                           )
    await message.delete()


@dp.message_handler(commands=['random_quote'])
async def random_quote_command(message: types.Message):
    await message.answer('Кто это тут у нас любит философию?' + '❤️')
    await bot.send_sticker(message.from_user.id, sticker=RANDOM_QUOTE_STICKER_ID)
    await message.delete()


@dp.message_handler(commands=['random_thinker'])
async def random_thinker_command(message: types.Message):
    i = randrange(1, len(thinkers) + 1)
    await bot.send_photo(chat_id=message.chat.id,
                         photo=thinkers[i]['photo'])
    await bot.send_message(chat_id=message.chat.id,
                           text=text_about_thinker(i),
                           parse_mode='HTML',
                           reply_markup=inline_keyboard(i))
    await bot.send_location(chat_id=message.chat.id,
                            latitude=thinker_location(i)['latitude'],
                            longitude=thinker_location(1)['longitude'])
    await message.delete()


@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)


@dp.message_handler()
async def standard_message(message: types.Message):
    if message.text == '❤️':
        return await bot.send_photo(chat_id=message.chat.id,
                                    photo=thinkers[1]['photo'])
    return await bot.send_message(chat_id=message.chat.id,
                                  text='Q')


if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True
                           )
