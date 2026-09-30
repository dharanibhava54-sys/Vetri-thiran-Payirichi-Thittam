from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
INDEX_FILE = BASE_DIR / "templates" / "index.html"


@router.get("/")
async def home():
    return FileResponse(INDEX_FILE)


@router.get("/health")
async def health():
    return {"status": "healthy"}