from pydantic import BaseModel, UUID4, Field
from datetime import datetime
import uuid


# modelo de schema de entrada para o produto
class BaseSchemaMixin(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
