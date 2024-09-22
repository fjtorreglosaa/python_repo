from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from database import Base
from models.author import Author

class AuthorEntity(Base):
    __tablename__ = "authors"

    id = Column(UNIQUEIDENTIFIER, primary_key=True)
    name = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    created_date = Column(DateTime, nullable = True)
    created_by = Column(UNIQUEIDENTIFIER, nullable=True)
    updated_date = Column(DateTime, nullable=True)
    updated_by = Column(UNIQUEIDENTIFIER, nullable=True)

    books = relationship("BookEntity", back_populates="author")

    def __init__(self, author: Author):
        self.id = author.id
        self.name = author.name
        self.nickname = author.nickname
        self.created_date = author.created_date
        self.created_by = author.created_by
        self.updated_date = author.updated_date
        self.updated_by = author.updated_by

    def to_model(self):
        return Author(
            id = self.id,
            name = self.name,
            nickname = self.nickname,
            created_date = self.created_date,
            created_by = self.created_by,
            updated_date = self.updated_date,
            updated_by = self.updated_by
        )