from api.contrib.models import BaseModel
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, Integer
from datetime import datetime

class CentroTreinamentoModel(BaseModel):
    __table__ = "centro_treinamento"
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(20),unique=True ,nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    criado_em: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    
    atleta: Mapped['AtletaModel'] = relationship(back_populates='centro_treinamento')
