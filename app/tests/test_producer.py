import asyncio
import json
from aiokafka import AIOKafkaProducer

BOOTSTRAP_SERVERS = "localhost:9092"


async def main():
    producer = AIOKafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode()
    )

    await producer.start()

    message = {
        "email_id": "email-1",
        "subject": "Invoice overdue",
        "recipients": ["billing@company.com"],
        "body_path": "sample_email.txt"
    }

    await producer.send_and_wait(
        "incoming-emails",
        message
    )

    print("Email sent!")

    await producer.stop()


asyncio.run(main())