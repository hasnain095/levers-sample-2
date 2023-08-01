import logging
from typing import Any

from fastapi import APIRouter

from app.core.celery_app import celery_app
from app.worker import sync_notification


FORMAT = "%(levelname)s:\t%(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/notify")
async def notify(
    message: str
) -> Any:
    """
    Retrieve items.
    """
    celery_app.send_task("app.worker.notify", args=[], kwargs={})
    logger.info("Task completed")
    return {"result": "Success"}


@router.post("/notify-sync")
async def notify_sync(
    message: str
) -> Any:
    """
    Retrieve items.
    """
    result = sync_notification.run()
    final = result.get()
    logger.info("Called sync_notification")
    return {"result": str(final)}
