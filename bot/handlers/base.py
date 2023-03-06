from aiogram import types
from states.base import Form


async def send_hello(message: types.Message):
    await Form.name.set()
    await message.reply("Hi there! What's your name?")


async def send_help(message: types.Message):
    await message.reply('To view all commands, please, click on menu button.')


async def echo(message: types.Message):
    await message.answer(f'Echo: {message.text}')
