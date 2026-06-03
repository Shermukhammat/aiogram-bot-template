from .db_sessions import DbSessionMiddleware
from .user import UserMiddleware
from loader import dp, db


dp.update.middleware.register(DbSessionMiddleware(db))
dp.update.middleware.register(UserMiddleware(db))
