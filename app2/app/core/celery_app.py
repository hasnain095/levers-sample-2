from app.core.config import settings
from celery import Celery

celery_app = Celery("worker", broker=settings.RABBITMQURL, backend="rpc://")

celery_app.conf.task_routes = {
    "app.worker.notify": "main-queue-app-2",
    "app.worker.notify_sch": "main-queue-app-2"
}
celery_app.conf.timezone = 'UTC'
celery_app.conf.beat_schedule = {
    'add-every-3-seconds': {
        'task': 'app.worker.notify_sch',
        'schedule': 180.0
    },
}
