from pydantic import  Field
from typing import Annotated
from api.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome da Categoria', examples='Muay-Thai', max_length=20)]
   