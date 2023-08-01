import json
import logging

import aio_pika

logger = logging.getLogger(__name__)


async def on_message(message: aio_pika.IncomingMessage) -> None:
    logger.info(message.body)
    print(" [x] Received message %r" % message)
    print("Message body is: %r" % message.body)
