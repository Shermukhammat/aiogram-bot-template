from .db_sessions import DbSessionMiddleware
from loader import dp, db


dp.update.middleware.register(DbSessionMiddleware(db))
