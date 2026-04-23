from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dao import CoinDAO


class CoinRepository:
    @classmethod
    async def get_by_symbol(cls, session: AsyncSession, symbol: str):
        return await CoinDAO.get_by_symbol(session, symbol)

    @classmethod
    async def get_or_create(
        cls, session: AsyncSession, symbol: str, name: str
    ):
        coin = await CoinDAO.get_by_symbol(session, symbol)
        if not coin:
            coin = await CoinDAO.create(session, symbol=symbol, name=name)
            await session.commit()
        return coin
