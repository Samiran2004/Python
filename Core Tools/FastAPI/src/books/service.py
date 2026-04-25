from sqlalchemy.ext.asyncio.session import AsyncSession
from schemas import BookCreateModel, BookUpdateModel
from sqlmodel import select, desc
from models import Book

class BookService:

    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))

        result = session.execute(statement=statement)

        return result.all() #type:ignore

    async def get_book(self, book_uid: str, session: AsyncSession):
        pass

    async def create_new_book(self, book_data: BookCreateModel, session: AsyncSession):
        pass

    async def update_book(self, book_data: BookUpdateModel, session: AsyncSession):
        pass

    async def delete_book(self, book_uid: str, session: AsyncSession):
        pass
