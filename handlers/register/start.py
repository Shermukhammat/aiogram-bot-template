from aiogram import types
from aiogram.filters import Command
from . import r

@r.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Hello! I am a bot.")