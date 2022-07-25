# Recipe-App-Api

## Neste repositório se encontra um projeto ainda em desenvolvimento, de uma API para gerenciar receitas.
### A stack

[x] - Python <br>
[x] - Django <br>
[x] - Django Rest Framework <br>
[x] - Docker <br>
[x] - Docker Compose <br>
[x] - PostgreSQL <br>
[x] - TDD(Testes) <br>

### Para Executar este projeto em sua máquina, é necessário que você tenha o docker e docker compose instalado.

Primeiro execute o comando a baixo para criar o container docker:

```
docker compose build
```

Em seguida execute o container com a aplicação utilizando o comando abaixo:

```
docker-compose up
```

### Comandos que podem ser necessários em uma aplicação que utiliza o Docker e Docker Compose:

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

## Comandos personalizados

```
docker compose run --rm app sh -c "python manage.py wait_for_db"
```