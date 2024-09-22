import datetime
from uuid import UUID
from models.model import Model

class Book(Model):
    def __init__(
            self,
            id: UUID,
            name: str,
            genre: str,
            total_pages: int,
            isbn: str,
            author_id: UUID,
            created_date: datetime = None,
            created_by: UUID = None,
            updated_date: datetime = None,
            updated_by: UUID = None):
        super().__init__(id, created_date, created_by, updated_date, updated_by)
        self.name: str = name
        self.genre: str = genre
        self.total_pages: str = total_pages
        self.isbn: str = isbn
        self.author_id: UUID = author_id