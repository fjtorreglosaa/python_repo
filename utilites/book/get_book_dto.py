from dataclasses import dataclass
import datetime
from uuid import UUID
from pydantic import BaseModel, Field, SkipValidation

@dataclass
class GetBookDto(BaseModel):
    id: UUID = Field(..., alias="Id")
    name: str = Field(..., alias="Book Name")
    genre: str = Field(..., alias="Genre")
    total_pages: int = Field(..., alias="Total Pages")
    isbn: str = Field(..., alias="ISBN")
    author_id: UUID = Field(..., alias="Author Id")
    created_date: SkipValidation[datetime.datetime] = Field(..., alias="Created Date")

    class Config:
        populate_by_name = True
        by_alias = True
        arbitrary_types_allowed = True