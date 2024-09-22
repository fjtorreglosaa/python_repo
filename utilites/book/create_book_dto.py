from dataclasses import dataclass
from uuid import UUID
from pydantic import BaseModel, Field

@dataclass
class CreateBookDto(BaseModel):
    book_name: str = Field(..., alias="Book Name")
    isbn: str = Field(..., alias="ISBN")
    author_id: UUID = Field(..., alias="Author Id")

    class Config:
        populate_by_name = True
        by_alias = True
        arbitrary_types_allowed = True