from typing import Any, Awaitable, Callable, Dict, Set
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from db import DataBase
import inspect


# Cache which handlers actually need a session so we only call
# inspect.signature() once per unique handler, not on every update.
_handlers_needing_session: Set[int] = set()
_handlers_checked: Set[int] = set()


class DbSessionMiddleware(BaseMiddleware):
    def __init__(self, db: DataBase):
        self.db = db

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        callback = data["handler"].callback
        cb_id = id(callback)

        if cb_id not in _handlers_checked:
            _handlers_checked.add(cb_id)
            if "session" in inspect.signature(callback).parameters:
                _handlers_needing_session.add(cb_id)

        if cb_id in _handlers_needing_session:
            # `async with` guarantees the session is closed and the
            # connection is returned to the asyncpg pool — even on error.
            async with self.db.session_maker() as session:
                data["session"] = session
                return await handler(event, data)

        return await handler(event, data)