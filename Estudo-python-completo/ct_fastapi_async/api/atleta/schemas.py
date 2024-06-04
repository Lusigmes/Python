from pydantic import Field, PositiveFloat
from typing import Annotated
from api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta', examples='Luis', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta', examples='12345678910', max_length=11)]
    idade: Annotated[str, Field(description='IDADE do Atleta', examples=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', examples=70.5)]
    alturas: Annotated[PositiveFloat, Field(description='Altura do Atleta', examples=1.74)]
    sexo: Annotated[str, Field(description='SEXO do Atleta', examples='M', max_length=1)]