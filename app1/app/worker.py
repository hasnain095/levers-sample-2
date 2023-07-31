import logging

from .main import celery_app
from app.core.config import settings

logger = logging.getLogger(__name__)


@celery_app.task()
def notify(word: str) -> str:
	logger.error(word)
	return f"test task return {word}"