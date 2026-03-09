from pydantic import BaseModel
from typing import List
from uuid import UUID
from app.domain.enums import EmailClassification

class IncomingEmailMessage(BaseModel):
    email_id: str
    recipients: List[str]
    subject: str
    body_path: str


class EmailClassificationMessage(BaseModel):
    email_id: str
    classification: EmailClassification


class EmailSummaryMessage(BaseModel):
    email_id: str
    summary: str