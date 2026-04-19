from enum import StrEnum

from pydantic_settings import BaseSettings, SettingsConfigDict

from app import ENV_FILE


class LogLevel(StrEnum):
	DEBUG = "DEBUG"
	INFO = "INFO"
	WARNING = "WARNING"
	ERROR = "ERROR"


class AppEnvironment(StrEnum):
	DEV = "dev"
	PROD = "prod"


class Config(BaseSettings):
	model_config = SettingsConfigDict(
		env_file=ENV_FILE,
		env_file_encoding="utf-8",
		extra="ignore",
	)

	# Redis
	redis_host: str
	redis_port: int
	redis_password: str
	redis_db_cache: int
	redis_db_alerts: int

	# PostgreSQL
	postgres_user: str
	postgres_password: str
	postgres_db: str
	postgres_host: str
	postgres_port: int

	# Logging
	log_level: LogLevel
	log_level_file: LogLevel

	# Environment
	app_environment: AppEnvironment
	debug: bool

	def build_db_url(self) -> str:
		"""Build SQLAlchemy URL scheme

		Returns:
			str: URL scheme
		"""
		return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
