from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dao import UserDAO


class UserRepository:
    @classmethod
    async def get_or_create(cls, session: AsyncSession, tg_id: int):
        user = await UserDAO.get_by_telegram_id(session, tg_id)
        if not user:
            user = await UserDAO.create(session, telegram_id=tg_id)
            await session.commit()
        return user
