from aiogram import types
from aiogram.filters import Command
from db.models import User
from . import r

@r.message(Command("start"))
async def start_handler(message: types.Message, session, user: User):
    await message.answer("Hello! I am a bot.")