from fastapi import FastAPI
from .config import settings
from .books.routes import book_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION
)

app.include_router(book_router, prefix=f"/api/{settings.VERSION}/books", tags=['books'])