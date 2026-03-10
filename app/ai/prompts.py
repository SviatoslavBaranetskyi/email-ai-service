CLASSIFICATION_PROMPT = """
Classify this email into one of the following types:
1. INVOICE - if the email is related to invoices, payments, or billing
2. MEETING - if the email is related to meetings, schedules, or planning
3. OTHER - everything else

Email:
Subject: {subject}
Body: {body}

Return only one of these options: INVOICE, MEETING, OTHER
"""

SUMMARY_PROMPT = """
Write a short summary of this email in 2-3 sentences.

Email:
Subject: {subject}
Body: {body}
"""