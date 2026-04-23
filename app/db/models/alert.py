from uuid import uuid4

from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import Base, TimestampMixin


class Alert(TimestampMixin, Base):
    __tablename__ = "alerts"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid4())
    )
    telegram_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.telegram_id")
    )
    coin_id: Mapped[int] = mapped_column(
        ForeignKey("coins.id"), nullable=False
    )
    coin = relationship("Coin", back_populates="alerts")

    upper_bound: Mapped[float | None] = mapped_column(nullable=True)
    lower_bound: Mapped[float | None] = mapped_column(nullable=True)

    percent_threshold: Mapped[float | None] = mapped_column(nullable=True)
    base_price: Mapped[float | None] = mapped_column(nullable=True)

    is_active: Mapped[bool] = mapped_column(default=True)
    user = relationship("User", back_populates="alerts")
