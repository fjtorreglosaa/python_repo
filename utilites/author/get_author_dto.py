from dataclasses import dataclass
import datetime
from uuid import UUID
from pydantic import BaseModel, Field, SkipValidation

@dataclass
class GetAuthorDto(BaseModel):
    id: UUID = Field(..., alias="Id")
    name: str = Field(..., alias="Author Name")
    nickname: str = Field(..., alias="Nickname")
    created_date: SkipValidation[datetime.datetime] = Field(..., alias="Created Date")

    class Config:
        populate_by_name = True
        by_alias = True
        arbitrary_types_allowed = True