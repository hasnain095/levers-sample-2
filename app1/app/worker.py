from app.core.celery_app import celery_app

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@celery_app.task()
def sync_notification() -> None:
    logger.info("Called sync_notification")
    result = "OK"
    result = celery_app.send_task("app.worker.notify_sync")
    return result
