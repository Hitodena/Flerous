from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import Base, IDMixin, TimestampMixin


class Coin(IDMixin, TimestampMixin, Base):
	__tablename__ = "coins"

	symbol: Mapped[str] = mapped_column(unique=True, nullable=False)  # BTCUSDT
	name: Mapped[str] = mapped_column(nullable=False)  # Bitcoin
	alerts = relationship("Alert", back_populates="coin")
