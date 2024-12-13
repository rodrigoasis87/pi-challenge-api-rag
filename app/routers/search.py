from fastapi import APIRouter
from app.models.schemas import SearchRequest, AskRequest
from app.services.search import search_documents, generate_answer

router = APIRouter()

@router.post("/")
async def search(data: SearchRequest):
    results = search_documents(data.query)
    return {"results": results}

@router.post("/ask")
async def ask(data: AskRequest):
    answer = generate_answer(data.question)
    return {"question": data.question, "answer": answer}