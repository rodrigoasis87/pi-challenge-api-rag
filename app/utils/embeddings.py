import cohere
from config import COHERE_API_KEY, EMBEDDING_MODEL
from app.utils.database import collection

cohere_client = cohere.Client(COHERE_API_KEY)

def generate_query_embeddings(query: str):
    return cohere_client.embed(texts=[query], model=EMBEDDING_MODEL).embeddings[0]

def generate_document_embeddings(document_id: str, content: str):
    embedding = cohere_client.embed(texts=[content], model=EMBEDDING_MODEL).embeddings[0]
    collection.update(ids=[document_id], embeddings=[embedding])