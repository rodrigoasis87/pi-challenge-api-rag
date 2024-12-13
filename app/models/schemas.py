from pydantic import BaseModel

class UploadRequest(BaseModel):
    title: str
    content: str

class GenerateEmbeddingsRequest(BaseModel):
    document_id: str

class SearchRequest(BaseModel):
    query: str

class AskRequest(BaseModel):
    question: str

class SearchResult(BaseModel):
    document_id: str
    title: str
    content_snippet: str
    similarity_score: float