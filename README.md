# Recipe App Api

## This project developed in Python, consists of an API to manage recipes.
### Stack

- Python <br>
- Django <br>
- Django Rest Framework <br>
- Docker <br>
- Docker Compose <br>
- PostgreSQL <br>
- Automated Tests(TDD) <br>

## Tests description

<img src="https://github.com/luisgs7/images-projects/blob/main/recipe-app-api/01.png">

## API routes
<br>...

### To run this project on your machine, you must have docker and docker compose installed.

First run the command below to create the docker container:

```
docker compose build
```

Then run the container with the application using the command below:

```
docker-compose up
```

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