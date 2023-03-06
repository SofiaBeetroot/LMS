import os
from random import choice
from aiogram import types

PHOTO_DIR = os.path.dirname(__file__).replace('handlers', 'photo')


async def get_random_picture(message: types.Message):
    random_picture = choice(os.listdir(PHOTO_DIR))
    with open(os.path.join(PHOTO_DIR, random_picture), 'rb') as photo:
        await message.reply_photo(photo, caption='This is your random pick \U0001F916')
