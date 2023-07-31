import logging
import datetime

from .main import celery_app
from app.core.config import settings

logger = logging.getLogger(__name__)


@celery_app.task()
def notify() -> str:
	date_time = datetime.datetime.now()
	logger.info(f"async notify task processed at {date_time}")
