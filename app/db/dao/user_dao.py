from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dao.base_dao import BaseDAO
from app.db.models import User


class UserDAO(BaseDAO[User]):
    model = User

    @classmethod
    async def get_by_telegram_id(
        cls, session: AsyncSession, tg_id: int
    ) -> User | None:
        logger.debug(
            "Finding User instance by telegram ID",
            model=cls.model,
            tg_id=tg_id,
        )
        stmt = select(cls.model).where(cls.model.telegram_id == tg_id)
        try:
            result = (await session.execute(stmt)).scalar_one_or_none()
            if result:
                logger.info(
                    "Successfully found User instance",
                    model=cls.model,
                    instance=result,
                    tg_id=tg_id,
                )
                return result
            return None
        except Exception as exc:
            logger.exception(
                "Failed to get User instance",
                error=exc,
                model=cls.model,
                tg_id=tg_id,
            )
