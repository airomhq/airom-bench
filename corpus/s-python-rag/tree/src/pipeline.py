"""Answer support tickets with retrieval over the product handbook."""

from openai import OpenAI
from sentence_transformers import SentenceTransformer
import chromadb

EMBEDDER = SentenceTransformer("all-MiniLM-L6-v2")
client = OpenAI()
store = chromadb.PersistentClient(path="./index")
collection = store.get_or_create_collection("handbook")


def embed(chunks: list[str]) -> list[list[float]]:
    return EMBEDDER.encode(chunks).tolist()


def answer(question: str) -> str:
    hits = collection.query(query_embeddings=embed([question]), n_results=4)
    context = "\n".join(hits["documents"][0])
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.1,
        max_tokens=400,
        messages=[{"role": "user", "content": f"{context}\n\n{question}"}],
    )
    return resp.choices[0].message.content
