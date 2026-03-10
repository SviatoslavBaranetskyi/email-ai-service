CREATE TABLE IF NOT EXISTS email_results (
    email_id TEXT PRIMARY KEY,
    classification TEXT,
    summary TEXT,
    status TEXT,
    created_at TIMESTAMP DEFAULT now()
);