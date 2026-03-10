import asyncio

from app.config import settings
from app.db.database import db

from app.messaging.kafka_producer import KafkaProducer
from app.messaging.kafka_consumer import KafkaConsumer
from app.messaging.kafka_utils import create_topics

from app.storage.local_blob_storage import LocalBlobStorage
from app.services.email_processor import EmailProcessor
from app.ai.agent import EmailAI
from app.repository.email_repository import EmailRepository


async def main():
    await create_topics(
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        topics=[
            settings.INCOMING_TOPIC,
            settings.CLASSIFICATION_TOPIC,
            settings.SUMMARY_TOPIC,
        ],
    )

    await db.connect()

    producer = KafkaProducer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()

    blob_storage = LocalBlobStorage(base_path="blobs")
    ai_agent = EmailAI()
    repository = EmailRepository()

    processor = EmailProcessor(
        blob_storage=blob_storage,
        ai_agent=ai_agent,
        repository=repository,
        producer=producer,
        classification_topic=settings.CLASSIFICATION_TOPIC,
        summary_topic=settings.SUMMARY_TOPIC,
    )

    consumer = KafkaConsumer(
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        topic=settings.INCOMING_TOPIC,
        processor=processor,
    )

    try:
        await consumer.start()
    finally:
        await producer.stop()
        await db.close()


if __name__ == "__main__":
    asyncio.run(main())