import asyncio
from app.ai.agent import EmailAI
from app.domain.enums import EmailClassification

async def test_email_ai():
    ai_agent = EmailAI()

    test_cases = [
        {
            "subject": "Invoice for March",
            "body": "Please find attached the invoice for your recent order. Payment is due in 30 days.",
            "expected_class": EmailClassification.INVOICE
        },
        {
            "subject": "Team Meeting Schedule",
            "body": "Let's schedule a meeting to discuss the Q2 roadmap and priorities.",
            "expected_class": EmailClassification.MEETING
        },
        {
            "subject": "Hello friend",
            "body": "Just wanted to say hi and see how you are doing!",
            "expected_class": EmailClassification.OTHER
        }
    ]

    for i, case in enumerate(test_cases, 1):
        classification, summary = await ai_agent.process_email(case["subject"], case["body"])
        print(f"Test case {i}:")
        print(f"Subject: {case['subject']}")
        print(f"Expected classification: {case['expected_class'].name}, Got: {classification.name}")
        print(f"Summary: {summary}\n")

        assert classification == case["expected_class"], f"Classification mismatch in test case {i}"

if __name__ == "__main__":
    asyncio.run(test_email_ai())