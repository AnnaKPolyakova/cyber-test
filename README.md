# cyber-test

Technologies and requirements:  

Python 3.10  
django 4.2.7  
Poetry  
Postgresql  

### About

API for app todo list

1) Users:  
Any can register a user and receive a token for him

2) Tasks: 
Any registered user can:  
- create, delete his own task, 
- get a list of  his tasks, 
- get information about his task by id  

3) Jobs: 
Any registered user can:
- the user can add, change, delete job to his task
- get a list of  his job with filter by task, 
- get information about his task by id
"is_done" field is set to automatic based on the value in the field "done_at"

Admin panel available

### Instruction for local run
* `Create .env file using .env_example_for_local`
* `python3 -m venv venv` - create venv 
* `source venv/bin/activate` - activate venv  
* `pip install poetry` - install poetry
* `poetry install` - install requirements
* `docker network create todolist` - create network
* `docker-compose -f docker-compose-local.yaml up -d --build` - run 
  postgresql in docker container
* `python3 manage.py migrate --settings=config.settings_local` - migrate
* `python3 manage.py createsuperuser --settings=config.settings_local` - to create superuser
* `python3 manage.py runserver --settings=config.settings_local` - run app
* `pytest` - run tests

#### To stop the container and remove volumes:

* `docker-compose -f docker-compose-local.yaml down --rmi all --volumes`

### Instruction for run all app in docker containers

* `Create .env file using .env_example_for_docker`
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
http://127.0.0.1:8000/api/v1/schema/redoc/  
http://127.0.0.1:8000/api/v1/schema/swagger/  

docker:  
http://127.0.0.1/api/v1/schema/redoc/  
http://127.0.0.1/api/v1/schema/swagger/  
