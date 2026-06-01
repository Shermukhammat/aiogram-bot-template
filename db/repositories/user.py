from db.models.user import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Sequence


class UserRepository:
    async def get(self, session: AsyncSession, id: int) -> User | None:
        result = await session.execute(select(User).where(User.id == id))
        return result.scalar_one_or_none()

    async def get_all(self, session: AsyncSession) -> Sequence[User]:
        result = await session.execute(select(User))
        return result.scalars().all()