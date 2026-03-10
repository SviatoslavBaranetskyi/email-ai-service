import json
from aiokafka import AIOKafkaConsumer
from app.schemas.kafka_messages import IncomingEmailMessage

class KafkaConsumer:
    def __init__(self, bootstrap_servers: str, topic: str, processor):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.processor = processor
        self.consumer: AIOKafkaConsumer = None

    async def start(self):
        self.consumer = AIOKafkaConsumer(
            self.topic,
            bootstrap_servers=self.bootstrap_servers,
            value_deserializer=lambda v: json.loads(v.decode("utf-8"))
        )
        await self.consumer.start()
        try:
            async for msg in self.consumer:
                await self.handle_message(msg.value)
        finally:
            await self.consumer.stop()

    async def handle_message(self, msg_dict: dict):
        message = IncomingEmailMessage(**msg_dict)
        await self.processor.process_email(message)

        print(f"Processed email_id={message.email_id}")