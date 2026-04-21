from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import Base, TimestampMixin


class User(TimestampMixin, Base):
	__tablename__ = "users"

	telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
	alerts = relationship("Alert", back_populates="user")
