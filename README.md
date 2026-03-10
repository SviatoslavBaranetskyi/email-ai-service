# Email AI Service

A service for automatically classifying and summarizing incoming emails using AI (Llama + LangGraph) and Kafka.

## Requirements

Python 3.11+

PostgreSQL

Kafka

Docker & Docker Compose (for Kafka + DB services)

Dependencies installed via pyproject.toml

## Quick Start
1. Set up Python environment
```bash 
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate # Windows
source venv/bin/activate # Mac/Linux

# Install dependencies
pip install -e .
```
2. Start PostgreSQL and Kafka with Docker Compose
```bash 
docker-compose up -d
```
Make sure your .env file is configured

3. Run the service
```bash
python app/main.py
```

The service will:

- Create Kafka topics if they don’t exist
- Connect to PostgreSQL
- Start consuming messages from INCOMING_TOPIC

## Test AI agent

This will run sample emails through the AI and print classification + summary.

```bash
python app/tests/test_agent.py
```

## Test Kafka producer
This sends test emails to INCOMING_TOPIC. Check main.py logs to see processing results.
```bash
python app/tests/test_producer.py
```

## Notes

Specify the Llama model in agent.py (llama2 or llama3).

Run Ollama local server if using a local Llama model:

```bash 
ollama pull llama3
```

Kafka topics are created automatically at service start.