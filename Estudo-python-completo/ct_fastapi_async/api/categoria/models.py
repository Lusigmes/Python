from api.contrib.models import BaseModel
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime
from datetime import datetime

class CategoriaModel(BaseModel):
    __table__ = "categoria"
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(20), nullable=False)
    criado_em: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    
    atleta: Mapped['AtletaModel'] = relationship(back_populates='categoria')
