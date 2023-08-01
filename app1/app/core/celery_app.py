from app.core.config import settings
from celery import Celery

celery_app = Celery("worker", broker=settings.RABBITMQURL, backend="rpc://")

celery_app.conf.task_routes = {
    "app.worker.sync_notification": "main-queue-app-1",
    "app.worker.notify": "main-queue-app-2",
    "app.worker.notify_sync": "queue-app-2-sync"
}
