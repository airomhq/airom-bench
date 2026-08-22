CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE document_chunks (
    id BIGSERIAL PRIMARY KEY,
    body TEXT NOT NULL,
    embedding vector(1536)
);

CREATE INDEX ON document_chunks USING hnsw (embedding vector_cosine_ops);
