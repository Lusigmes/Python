from pydantic import Field
from typing import Annotated
from api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', examples='CT Maximum', max_length=20)]
    endererco: Annotated[str, Field(description='Endereço do CT', examples='Luis', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietario do CT', examples='Rayssa', max_length=30)]
