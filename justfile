# https://just.systems/
set dotenv-load := false

@_default:
    just --list

setup:
    pre-commit install
    cp -i .env.example .env
    docker compose build
    docker compose run --rm web bash -c "createdb -U postgres -h db -p 5432 django-dash"

@build:
    docker compose down
    docker compose build

@run:
    docker compose up

@serve-js:
    cd frontend && \
    NODE_ENV='development' npm run dev

@console:
    docker compose run --rm web bash

@djshell:
    docker compose run --rm web bash -c "pipenv run src/manage.py shell"

@add-dep depName:
    docker compose run --rm web bash -c "pipenv install {{depName}}"

@migrate:
    docker compose run --rm web bash -c "pipenv run src/manage.py migrate"

@test:
    docker compose run --rm web bash -c "pipenv run pytest -vv src"

@interactive_server:
    docker compose stop web
    docker compose run --service-ports --use-aliases web bash -c "pipenv run src/manage.py runserver 0.0.0.0:8000"
