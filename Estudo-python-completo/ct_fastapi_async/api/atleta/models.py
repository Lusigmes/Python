from api.contrib.models import BaseModel
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, DateTime, ForeignKey
from datetime import datetime

class AtletaModel(BaseModel):
    __table__ = "atleta"
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    criado_em: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atleta')
    categoria_id = Mapped[int] = mapped_column(ForeignKey('categoria.pk_id'))
    
    categoria: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atleta')
    centro_treinamento_id = Mapped[int] = mapped_column(ForeignKey('centro_treinamento.pk_id'))