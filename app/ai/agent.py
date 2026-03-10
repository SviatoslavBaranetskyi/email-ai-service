from app.domain.enums import EmailClassification

class EmailAI:
    async def classify_email(self, subject: str, body: str) -> EmailClassification:
        subject_lower = subject.lower()
        body_lower = body.lower()

        if "invoice" in subject_lower or "payment" in body_lower:
            return EmailClassification.INVOICE
        elif "meeting" in subject_lower or "schedule" in body_lower:
            return EmailClassification.MEETING
        else:
            return EmailClassification.OTHER

    async def summarize_email(self, subject: str, body: str) -> str:
        summary = body[:100] + "..." if len(body) > 100 else body
        return summary