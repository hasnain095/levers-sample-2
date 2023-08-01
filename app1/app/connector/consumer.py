import logging

import aio_pika

logger = logging.getLogger(__name__)


async def on_message(message: aio_pika.IncomingMessage):
    logger.info(message)
