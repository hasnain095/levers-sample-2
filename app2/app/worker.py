import datetime

from app.core.celery_app import celery_app

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@celery_app.task()
def notify() -> str:
    date_time = datetime.datetime.now()
    logger.info(f"async notify task processed at {date_time}")


@celery_app.task()
def notify_sync() -> str:
    date_time = datetime.datetime.now()
    log_message = f"async notify task processed at {date_time}"
    logger.info(log_message)
    return log_message


@celery_app.task()
def notify_sch() -> str:
    date_time = datetime.datetime.now()
    log_message = f"async notify task processed at {date_time}"
    logger.info(log_message)
    return log_message
