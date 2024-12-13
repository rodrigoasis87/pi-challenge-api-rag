import os
from dotenv import load_dotenv

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "embed-multilingual-v2.0")

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORIAS_PDF_PATH = os.path.join(ROOT_DIR, "Historias.pdf")

if not os.path.exists(HISTORIAS_PDF_PATH):
    raise FileNotFoundError(f"El archivo Historias.pdf no se encontró en {HISTORIAS_PDF_PATH}") 