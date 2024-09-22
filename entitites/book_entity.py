from sqlalchemy import Column, ForeignKey, Numeric, String, DateTime, Integer
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from database import Base
from models.book import Book

class BookEntity(Base):
    __tablename__ = "books"

    id = Column(UNIQUEIDENTIFIER, primary_key=True)
    name = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    total_pages = Column(Integer().with_variant(Numeric(10, 0), "mssql"), nullable=False)
    isbn = Column(String, nullable=True)
    author_id = Column(UNIQUEIDENTIFIER, ForeignKey("authors.id"), nullable=False)
    created_date = Column(DateTime, nullable = True)
    created_by = Column(UNIQUEIDENTIFIER, nullable=True)
    updated_date = Column(DateTime, nullable=True)
    updated_by = Column(UNIQUEIDENTIFIER, nullable=True)

    def __init__(self, book: Book):
        self.id = book.id
        self.name = book.name
        self.genre = book.genre
        self.total_pages = book.total_pages
        self.isbn = book.isbn
        self.author_id = book.author_id
        self.created_date = book.created_date
        self.created_by = book.created_by
        self.updated_date = book.updated_date
        self.updated_by = book.updated_by
    
    author = relationship("AuthorEntity", back_populates="books")

    def to_model(self):
        return Book(
            id = self.id,
            name = self.name,
            genre = self.genre,
            total_pages = self.total_pages,
            isbn = self.isbn,
            author_id = self.author_id,
            created_date = self.created_date,
            created_by = self.created_by,
            updated_date = self.updated_date,
            updated_by = self.updated_by
        )