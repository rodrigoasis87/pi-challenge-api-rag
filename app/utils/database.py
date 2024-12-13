import chromadb

# Crear el cliente de ChromaDB con almacenamiento en memoria
client = chromadb.Client()

# Crear o recuperar la colección de documentos
collection = client.get_or_create_collection(name="documents")

def add_document(document_id: str, content: str, metadata: dict):
    collection.add(documents=[content], metadatas=[metadata], ids=[document_id])

def get_document_by_id(document_id: str):
    result = collection.get(ids=[document_id])
    if not result["documents"]:
        return None
    return {
        "id": result["ids"][0],
        "content": result["documents"][0],
        "metadata": result["metadatas"][0]
    }

def query_documents(embedding: list, top_n: int = 5):
    results = collection.query(query_embeddings=[embedding], n_results=top_n)
    return [
        {
            "id": result_id,
            "content": document,
            "metadata": metadata,
            "score": score
        }
        for result_id, document, metadata, score in zip(
            results["ids"], results["documents"], results["metadatas"], results["distances"]
        )
    ]