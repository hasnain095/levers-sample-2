import logging
import aio_pika

from app.core.config import settings

logger = logging.getLogger(__name__)


async def sender(queue: str, body: str):
    connection = await aio_pika.connect(settings.RABBITMQURL)

    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(queue)
        await channel.default_exchange.publish(
            aio_pika.Message(bytes(body, 'utf-8')),
            routing_key=queue.name,
        )
