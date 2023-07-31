import logging
from typing import Any, List, Optional

from fastapi import APIRouter

from app.connector.sender import sender
from app.core.celery_app import celery_app


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
    celery_app.execute.send_task("app2.worker.notify", args=[], kwargs={})
    logger.info("logging from the root logger")
    # await sender(queue="app2", body=message)
    return {"status": "alive"}