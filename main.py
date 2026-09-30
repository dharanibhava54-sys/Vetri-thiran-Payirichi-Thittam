from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .config import settings
from .database import init_db
from .routes import router



@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title=settings.APP_NAME,
    description=(
        "AI-powered personalized fitness plan generator "
        "using Google Gemini."
    ),
    version="1.0.0",
    lifespan=lifespan,
)


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


app.include_router(router)