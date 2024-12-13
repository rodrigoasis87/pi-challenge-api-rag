from app.utils.embeddings import generate_query_embeddings
from app.utils.database import query_documents
import cohere
from config import COHERE_API_KEY

cohere_client = cohere.Client(COHERE_API_KEY)

def search_documents(query: str):
    query_embedding = generate_query_embeddings(query)

    # Verificar la dimensión de los embeddings
    collection_dimension = 768  # Dimensión esperada (ajustar según tu modelo)
    if len(query_embedding) != collection_dimension:
        raise ValueError(f"Dimensión del embedding incorrecta: {len(query_embedding)}, se esperaba: {collection_dimension}")

    results = query_documents(query_embedding)
    return [
        {
            "document_id": result["id"],
            "title": result["metadata"]["title"],
            "content_snippet": result["content"][:200],
            "similarity_score": result["score"]
        }
        for result in results
    ]

def generate_answer(question: str):
    question_embedding = generate_query_embeddings(question)
    results = query_documents(question_embedding)
    context = " ".join([result["content"] for result in results])
    response = cohere_client.generate(
        model="command-xlarge-nightly",
        prompt=f"Contexto: {context}\nPregunta: {question}\nRespuesta:",
        max_tokens=100
    )
    return response.generations[0].text.strip()