from enum import Enum

class EmailClassification(str, Enum):
    SPAM = "spam"
    INVOICE = "invoice"
    MEETING = "meeting"
    PERSONAL = "personal"
    OTHER = "other"

class ProcessingStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"