from fastapi import APIRouter, status
from typing import List
from .books_data import books
from .schemas import Book, BookUpdateModel
from fastapi.exceptions import HTTPException

book_router = APIRouter()

@book_router.get('/', response_model=List[Book])  #* For get all books...
async def get_all_books():
    return books

@book_router.get('/{book_id}')  #* For get a book by id...
async def get_book_by_id(book_id: int)-> dict:
    for book in books:
      if book["id"] == book_id:
         return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found!")

@book_router.post('/', status_code=status.HTTP_201_CREATED)  #* For create new book...
async def create_new_book(book_data: Book)-> Book:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book # type: ignore

@book_router.patch('/{book_id}', status_code=status.HTTP_200_OK)  #* For update a book...
async def update_book(book_id: int, book_update_data: BookUpdateModel): # type: ignore
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['author'] = book_update_data.author
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language

            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found!")


@book_router.delete('/{book_id}', status_code=status.HTTP_200_OK)  #* For delete a book...
async def update_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)

            return {}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found!")
