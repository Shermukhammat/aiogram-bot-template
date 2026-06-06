from .db_sessions import DbSessionMiddleware
from .user import UserMiddleware
from .subscription import CheckSubscriptionMiddleware
from loader import dp, db


dp.update.middleware.register(DbSessionMiddleware(db))
dp.update.middleware.register(UserMiddleware(db))
dp.message.middleware.register(CheckSubscriptionMiddleware(db))
dp.callback_query.middleware.register(CheckSubscriptionMiddleware(db))
