import logging
import pika

logger = logging.getLogger(__name__)


def sender(queue:str, body: str):
	parameters = pika.URLParameters('amqp://guest:guest@rabbitmq:5672')
	connection = pika.BlockingConnection(parameters=parameters)
	channel = connection.channel()
	channel.queue_declare(queue=queue)
	channel.basic_publish('',
		queue,
		body,
		pika.BasicProperties(content_type='text/plain',delivery_mode=pika.DeliveryMode.Transient))
	logger.info(str(body))
	connection.close()