from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dao import AlertDAO


class AlertRepository:
    @classmethod
    async def create(
        cls,
        session: AsyncSession,
        telegram_id: int,
        coin_id: int,
        upper_bound: float | None = None,
        lower_bound: float | None = None,
        percent_threshold: float | None = None,
        base_price: float | None = None,
    ):
        alert = await AlertDAO.create(
            session,
            telegram_id=telegram_id,
            coin_id=coin_id,
            upper_bound=upper_bound,
            lower_bound=lower_bound,
            percent_threshold=percent_threshold,
            base_price=base_price,
        )
        await session.commit()
        return alert

    @classmethod
    async def get_active_by_symbol(cls, session: AsyncSession, symbol: str):
        return await AlertDAO.get_all(session, symbol=symbol, is_active=True)

    @classmethod
    async def get_user_alerts(cls, session: AsyncSession, telegram_id: int):
        return await AlertDAO.get_all(session, telegram_id=telegram_id)

    @classmethod
    async def deactivate(cls, session: AsyncSession, alert_id: str) -> None:
        await AlertDAO.deactivate(session, alert_id)
        await session.commit()
