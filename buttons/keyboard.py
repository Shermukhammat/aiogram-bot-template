from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class Keyboards:

    @staticmethod
    def admin_panel():
        return ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="📢 Xabar yuborish")],
            [KeyboardButton(text="📊 Statistika"), KeyboardButton(text="⚙️ Sozlamalar")],
            [KeyboardButton(text="⬅️ Chiqish")],
        ], resize_keyboard=True)
    
    @staticmethod
    def settings():
        return ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="📡 Kanallar"), KeyboardButton(text="👨🏻‍💻 Adminlar")],
            [KeyboardButton(text="⬅️ Orqaga")],
        ], resize_keyboard=True)

    @staticmethod
    def remove():
        return ReplyKeyboardRemove()


    @staticmethod
    def back(next: bool = False):
        if next:
            return ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton(text="➡️ Keyingi")],
                [KeyboardButton(text="⬅️ Orqaga")]
            ], resize_keyboard=True)
        return ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="⬅️ Orqaga")],
        ], resize_keyboard=True)

    @staticmethod
    def cancel():
        return ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="❌ Bekor qilish")],
        ], resize_keyboard=True)

    @staticmethod
    def confirm_send():
        return ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="🚀 Yuborish")],
            [KeyboardButton(text="⬅️ Orqaga"), KeyboardButton(text="❌ Bekor qilish")],
        ], resize_keyboard=True)