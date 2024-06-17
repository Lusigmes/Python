from decimal import Decimal
from bson import Decimal128
from pydantic import BaseModel, UUID4, Field
from datetime import datetime
import uuid


# modelo de schema de entrada para o produto
class BaseSchemaMixin(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    #    updated_at: datetime = Field(default_factory=ddatetime.now(UTC)


class OutSchema(BaseModel):
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

    def set_schema(cls, data):
        for key, value in data.items():
            if isinstance(value, Decimal128):
                data[key] = Decimal(str(value))

        return data
