import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))
    POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB = os.getenv("POSTGRES_DB", "email_service")

    KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")

    INCOMING_TOPIC = os.getenv("INCOMING_TOPIC")
    CLASSIFICATION_TOPIC = os.getenv("CLASSIFICATION_TOPIC")
    SUMMARY_TOPIC = os.getenv("SUMMARY_TOPIC")


settings = Settings()