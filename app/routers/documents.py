from fastapi import APIRouter, UploadFile, File, HTTPException
from app.models.schemas import UploadRequest, GenerateEmbeddingsRequest
from app.utils.database import add_document
from app.utils.embeddings import generate_document_embeddings
from app.utils.pdf_reader import extract_text_from_pdf
import uuid

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Solo se permiten archivos PDF.")

    try:
        # Procesar el archivo PDF
        text_content = extract_text_from_pdf(file.file)
        if not text_content:
            raise HTTPException(status_code=400, detail="El PDF no contiene texto legible.")
        
        # Generar un ID único y guardar en la base de datos
        document_id = str(uuid.uuid4())
        add_document(document_id=document_id, content=text_content, metadata={"title": file.filename})

        return {"message": "Documento cargado correctamente.", "document_id": document_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {e}")

@router.post("/generate-embeddings")
async def generate_embeddings(data: GenerateEmbeddingsRequest):
    from app.utils.database import get_document_by_id

    document = get_document_by_id(data.document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Documento no encontrado.")

    generate_document_embeddings(data.document_id, document["content"])
    return {"message": "Embeddings generados correctamente.", "document_id": data.document_id}