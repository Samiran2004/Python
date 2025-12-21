from pydantic import BaseModel

class Book(BaseModel):   #* Class for book respon...
   id: int
   title: str
   author: str
   publisher: str
   published_date: str
   page_count: int
   language: str

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str