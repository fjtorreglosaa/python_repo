from abc import ABC, abstractmethod
import datetime
from uuid import uuid4, UUID

class Model(ABC):
    def __init__(
            self,
            id: UUID,
            created_date: datetime = None,
            created_by: UUID = None,
            updated_date: datetime = None,
            updated_by: datetime = None
        ):
        self.id: UUID = id or uuid4()
        self.created_date: datetime = created_date
        self.created_by: UUID = created_by
        self.updated_date: datetime = updated_date
        self.updated_by: UUID = updated_by