# WorkoutAPI

Esta é uma API de competição de crossfit chamada WorkoutAPI. Nela, é possível criar, visualizar todos os usuários, editar, deletar e consultar um usuário pelo ID, assim como realizar operações semelhantes para categorias e centros de treinamento.

## Stack da API

A API foi desenvolvida utilizando o FastAPI (async), junto das seguintes bibliotecas: alembic, SQLAlchemy e Pydantic. Para salvar os dados, está sendo utilizado o Postgres por meio do Docker.

## Execução da API

Para executar o projeto, utilizei o pyenv com a versão 3.11.4 do Python para o ambiente virtual.

Caso opte por usar pyenv, após instalar, execute:

```bash
pyenv virtualenv 3.11.4 workoutapi
pyenv activate workoutapi
pip install -r requirements.txt
```
Para subir o banco de dados, caso não tenha o docker-compose instalado, faça a instalação e logo em seguida, execute:
```bash
make run-docker
```
Para criar uma nova migration, execute:
```bash
make create-migrations d="nome_da_migration"
```
Para criar o banco de dados, execute:
```bash
make run-migrations
```
Para subir a API, execute:
```bash
make run
```
