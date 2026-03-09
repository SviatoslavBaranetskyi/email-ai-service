from sqlalchemy import Column, String, Enum as SqlEnum, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import uuid
from app.domain.enums import EmailClassification, ProcessingStatus

Base = declarative_base()

class EmailProcessingResult(Base):
    __tablename__ = "email_processing_results"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email_id = Column(String, nullable=False, unique=True)
    classification = Column(SqlEnum(EmailClassification), nullable=False)
    summary = Column(Text, nullable=True)
    status = Column(SqlEnum(ProcessingStatus), default=ProcessingStatus.PENDING)