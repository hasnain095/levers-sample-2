import json
import logging

import aio_pika

from app.worker import test_celery

logger = logging.getLogger(__name__)

async def on_message(message: aio_pika.IncomingMessage) -> None:
	logger.error(message.body)
	task = test_celery.delay(message.body)
	logger.error("Result delay" + str(task))
	task = test_celery.run(message.body)
	logger.error("Result apply" + str(task))
	print(" [x] Received message %r" % message)
	print("Message body is: %r" % message.body)
