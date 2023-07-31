import json
import logging

import aio_pika  
import ast

logger = logging.getLogger(__name__)

async def on_message(message: aio_pika.IncomingMessage):
	logger.error(message)