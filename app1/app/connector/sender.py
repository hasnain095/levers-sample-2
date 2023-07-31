import logging
import aio_pika

logger = logging.getLogger(__name__)


async def sender(queue:str, body: str):
	# parameters = pika.URLParameters('amqp://guest:guest@rabbitmq:5672')
	# connection = pika.BlockingConnection(parameters=parameters)
	# channel = connection.channel()
	# channel.queue_declare(queue=queue)
	# channel.basic_publish('',
	# 	queue,
	# 	body,
	# 	pika.BasicProperties(content_type='text/plain',delivery_mode=pika.DeliveryMode.Transient))
	# logger.info(str(body))
	# connection.close()
	connection = await aio_pika.connect("amqp://guest:guest@rabbitmq:5672")
	
	async with connection:
        # Creating a channel
		channel = await connection.channel()
		queue = await channel.declare_queue(queue)
		await channel.default_exchange.publish(
	            aio_pika.Message(bytes(body, 'utf-8')),
	            routing_key=queue.name,
	        )