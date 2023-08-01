import asyncio
import aio_pika
from fastapi import FastAPI

from app.core.config import settings
from app.core.celery_app import celery_app
from app.connector.consumer import on_message


app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.on_event('startup')
async def startup():
    loop = asyncio.get_event_loop()
    connection = await aio_pika.connect(settings.RABBITMQURL, loop=loop)
    channel = await connection.channel()
    queue = await channel.declare_queue("app2")
    await queue.consume(on_message)

