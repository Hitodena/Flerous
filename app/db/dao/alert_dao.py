from loguru import logger
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dao.base_dao import BaseDAO
from app.db.models import Alert


class AlertDAO(BaseDAO[Alert]):
    model = Alert

    @classmethod
    async def deactivate(cls, session: AsyncSession, alert_id: str) -> None:
        logger.debug("Deactivating alert", model=cls.model, alert_id=alert_id)
        stmt = (
            update(cls.model)
            .where(cls.model.id == alert_id)
            .values(is_active=False)
        )
        try:
            await session.execute(stmt)
            logger.info(
                "Successfully deactivated alert",
                model=cls.model,
                alert_id=alert_id,
            )
        except Exception as exc:
            logger.exception(
                "Failed to deactivate alert",
                error=exc,
                model=cls.model,
                alert_id=alert_id,
            )
            raise
