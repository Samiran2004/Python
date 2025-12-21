from sqlmodel import text, SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import settings

engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True
)

async def init_db():
    async with engine.begin() as conn:
        from src.books.models import Book

        await conn.run_sync(
            SQLModel.metadata.create_all
        )