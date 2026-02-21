from sqlmodel import SQLModel, Field, Column
from datetime import datetime, date
import uuid
import sqlalchemy.dialects.postgresql as pg

class Book(SQLModel, table=True):
    __tablename__ = "books" #type:ignore
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4()
        )
    )
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime = Field(
        sa_column=Column(
        pg.TIMESTAMP,
        default=datetime.now
    ))
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )

    def __repr__(self) -> str:
        return f"<Book {self.title}>"