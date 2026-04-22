from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dao.base_dao import BaseDAO
from app.db.models import Coin


class CoinDAO(BaseDAO[Coin]):
    model = Coin

    @classmethod
    async def get_by_symbol(
        cls, session: AsyncSession, symbol: str
    ) -> Coin | None:
        logger.debug(
            "Finding Coin instance by symbol", model=cls.model, symbol=symbol
        )
        stmt = select(cls.model).where(cls.model.symbol == symbol)
        try:
            result = (await session.execute(stmt)).scalar_one_or_none()
            if result:
                logger.info(
                    "Successfully found Coin instance",
                    model=cls.model,
                    instance=result,
                    symbol=symbol,
                )
                return result
            return None
        except Exception as exc:
            logger.exception(
                "Failed to get Coin instance",
                error=exc,
                model=cls.model,
                symbol=symbol,
            )
