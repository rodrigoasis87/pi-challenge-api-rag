from fastapi import FastAPI
from app.routers import documents, search

app = FastAPI()

# Registrar los routers
app.include_router(documents.router, prefix="/documents", tags=["Documents"])
app.include_router(search.router, prefix="/search", tags=["Search"])

@app.get("/")
async def root():
    return {"message": "Bienvenido al API RAG"}