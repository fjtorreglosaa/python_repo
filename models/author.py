import datetime
from uuid import UUID
from models.model import Model

class Author(Model):
    def __init__(
            self,
            id: UUID,
            name: str,
            nickname: str,
            created_date: datetime = None,
            created_by: UUID = None,
            updated_date: datetime = None,
            updated_by: UUID = None):
        super().__init__(id, created_date, created_by, updated_date, updated_by)
        self.name: str = name
        self.nickname: str = nickname