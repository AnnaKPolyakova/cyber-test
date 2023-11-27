# cyber-test

Technologies and requirements:
Python 3.11
django 4.2.7
Poetry
Postgresql

### About

API for app todo list  

### To create .env
* `Create .env file using .env_example`  

### Instruction for local run
* `Create venv`
* `python3 -m venv venv` - create venv 
* `source venv/bin/activate` - activate venv  
* `pip install poetry` - install poetry
* `poetry install` - install requirements
* `docker network create todolist` - create network
* `docker-compose -f docker-compose-local.yaml up -d --build` - run 
  postgresql in docker container
* `python3 manage.py runserver --settings=config.settings_local` - run app
* `python3 manage.py migrate --settings=config.settings_local` - migrate
* `pytest` - run tests

#### To stop the container and remove volumes:

* `docker-compose -f docker-compose-local.yaml down --rmi all --volumes`

### Instruction for run all app in docker containers

* `docker network create todolist` - create network
* `docker-compose up -d --build` - run
* `docker-compose exec web python manage.py migrate --noinput` - migrate
* `docker-compose exec web python manage.py collectstatic --no-input` - 
  collect static
* `docker-compose exec web pytest` - createsuperuser
* `docker-compose exec web python manage.py createsuperuser` - createsuperuser


#### To stop the container and remove volumes:

* `docker-compose down --rmi all --volumes`

To open documentation:

local:  
http://127.0.0.1:8000/v1/doc/redoc/  
http://127.0.0.1:8000/v1/doc/swagger/  

docker:  
http://127.0.0.1/v1/doc/redoc/  
http://127.0.0.1/v1/doc/swagger/  
