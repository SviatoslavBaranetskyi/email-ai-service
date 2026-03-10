from app.domain.enums import ProcessingStatus
from app.db.database import db


class EmailRepository:
    async def save_processing_result(
        self,
        email_id: str,
        classification,
        summary: str,
        status: ProcessingStatus,
    ):
        async with db.pool.acquire() as conn:
            await conn.execute(
                """
                INSERT INTO email_results(email_id, classification, summary, status)
                VALUES($1, $2, $3, $4)
                ON CONFLICT (email_id) DO UPDATE
                SET classification = EXCLUDED.classification,
                    summary = EXCLUDED.summary,
                    status = EXCLUDED.status
                """,
                email_id,
                classification.name if classification else None,
                summary,
                status.name,
            )