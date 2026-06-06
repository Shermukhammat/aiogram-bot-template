from aiogram.fsm.state import State, StatesGroup


class AdminPanel(StatesGroup):
    main = State()
    