from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str,Field(description='Nome do atleta', examples='Joao', max_length=58)]
    cpf: Annotated[str,Field(description='CPF do atleta', examples='12345678900', max_length=11)]
    idade: Annotated[int,Field(description='Idade do atleta', examples=25,)]
    peso: Annotated[PositiveFloat,Field(description='Peso do atleta', examples='Joao', max_length=75.5)]
    altura: Annotated[PositiveFloat,Field(description='Altura do atleta', examples='1.70', max_length=1.70)]
    sexo: Annotated[str,Field(description='Sexo do atleta', examples='M', max_length=1)]