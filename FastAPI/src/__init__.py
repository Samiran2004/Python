from fastapi import FastAPI
from .config import settings
from .books.routes import book_router
from contextlib import asynccontextmanager
from .books.db.main import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Server is starting...")
    await init_db()
    yield
    print(f"Server has been stopped...")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    lifespan=life_span
)

app.include_router(book_router, prefix=f"/api/{settings.VERSION}/books", tags=['books'])