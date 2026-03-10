from app.storage.blob_storage import BlobStorage
from app.ai.agent import EmailAI
from app.repository.email_repository import EmailRepository
from app.messaging.kafka_producer import KafkaProducer
from app.schemas.kafka_messages import (
    IncomingEmailMessage,
    EmailClassificationMessage,
    EmailSummaryMessage,
)
from app.domain.enums import ProcessingStatus

class EmailProcessor:
    def __init__(
        self,
        blob_storage: BlobStorage,
        ai_agent: EmailAI,
        repository: EmailRepository,
        producer: KafkaProducer,
        classification_topic: str,
        summary_topic: str,
    ):
        self.blob_storage = blob_storage
        self.ai_agent = ai_agent
        self.repository = repository
        self.producer = producer
        self.classification_topic = classification_topic
        self.summary_topic = summary_topic

    async def process_email(
        self, message: IncomingEmailMessage
    ) -> None:
        try:
            body = self.blob_storage.read(message.body_path)
        except FileNotFoundError:
            await self.repository.save_processing_result(
                email_id=message.email_id,
                classification=None,
                summary=None,
                status=ProcessingStatus.FAILED,
            )
            raise

        classification = await self.ai_agent.classify_email(message.subject, body)
        summary = await self.ai_agent.summarize_email(message.subject, body)

        await self.repository.save_processing_result(
            email_id=message.email_id,
            classification=classification,
            summary=summary,
            status=ProcessingStatus.SUCCESS,
        )

        classification_msg = EmailClassificationMessage(
            email_id=message.email_id,
            classification=classification,
        )
        summary_msg = EmailSummaryMessage(
            email_id=message.email_id,
            summary=summary,
        )

        await self.producer.publish(self.classification_topic, classification_msg.dict())
        await self.producer.publish(self.summary_topic, summary_msg.dict())
