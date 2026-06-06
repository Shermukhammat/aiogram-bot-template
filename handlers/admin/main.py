from aiogram import types, F
from aiogram.filters import Command
from db.models import User
from loader import db
from buttons import Keyboards
from . import r



@r.message(Command('admin'))
async def show_admin_panel(update: types.Message, session, user: User):
    if not user.is_admin:
        return
    
    await update.answer("👨🏻‍💻 Admin panel", reply_markup=Keyboards.admin_panel())