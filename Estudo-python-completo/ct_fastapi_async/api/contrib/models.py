from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import UUID
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), nullable=False, default=uuid4)