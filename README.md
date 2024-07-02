# WorkoutAPI

Esta é uma API de competição de crossfit chamada WorkoutAPI (isso mesmo rs, eu acabei unificando duas coisas que gosto: codar e treinar). É uma API pequena, devido a ser um projeto mais hands-on e simplificado. Nós desenvolveremos uma API com poucas tabelas, mas com o necessário para você aprender como utilizar o FastAPI.

## Modelagem de Entidade e Relacionamento - MER

![MER](link_to_image)

## Stack da API

A API foi desenvolvida utilizando o FastAPI (async), junto das seguintes bibliotecas: alembic, SQLAlchemy e Pydantic. Para salvar os dados, está sendo utilizado o Postgres por meio do Docker.

## Execução da API

Para executar o projeto, utilizei o pyenv com a versão 3.11.4 do Python para o ambiente virtual.

Caso opte por usar pyenv, após instalar, execute:

```bash
pyenv virtualenv 3.11.4 workoutapi
pyenv activate workoutapi
pip install -r requirements.txt
