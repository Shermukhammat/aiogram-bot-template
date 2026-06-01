from .register import r as register_router
from .admin import r as admin_router
from loader import dp

dp.include_router(register_router)
dp.include_router(admin_router)