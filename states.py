from aiogram.fsm.state import State, StatesGroup


class AdminPanel(StatesGroup):
    main = State()
    

class AdsSending(StatesGroup):
    get_message = State()
    get_buttons = State()
    get_button_name = State()
    get_button_url = State()
    get_button_color = State()
    get_remove_button = State()
    confirm = State()