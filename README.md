# Recipe App Api

## This project developed in Python, consists of an API to manage recipes.
### Stack

- Python 
- Django 
- Django Rest Framework 
- Docker 
- Docker Compose 
- PostgreSQL 
- Automated Tests(TDD)
- Drf-spectacular 

## Tests description

<img src="https://github.com/luisgs7/images-projects/blob/main/recipe-app-api/01.png">

## API routes

### API routes to manage recipes

<img src="https://github.com/luisgs7/images-projects/blob/main/recipe-app-api/02.png">

<img src="https://github.com/luisgs7/images-projects/blob/main/recipe-app-api/03.png">

### API routes to manage users

<img src="https://github.com/luisgs7/images-projects/blob/main/recipe-app-api/04.png">


### To run this project on your machine, you must have docker and docker compose installed.

First run the command below to create the docker container:

```
docker compose build
```

Then run the container with the application using the command below:

```
docker-compose up
```
Para ler a Documentação da API, basta acessar: http://0.0.0.0:8000/api/docs/

### Useful commands in an application that uses Docker and Docker Compose:

```
docker build . 
```

```
docker compose build
```

```
docker compose run --rm app sh -c "flake8"
```

```
docker compose run --rm app sh -c "django-admin startproject app ."
```

```
docker-compose up
```

```
docker-compose down
```

```
docker compose run --rm app sh -c "python manage.py startapp core"
```

## Custom commands

```
docker compose run --rm app sh -c "python manage.py wait_for_db"
```
