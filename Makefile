ifneq (,$(wildcard ./.env))
	include .env
	export
	ENV_FILE_PARAM = --env-file .env
endif

build:
	docker-compose up --build -d --remove-orphans
	
up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs

migrate:
	docker-compose exec api python manage.py migrate
	
migrations:
	docker-compose exec api python manage.py makemigrations

superuser:
	docker-compose exec api python manage.py createsuperuser

db:
	docker-compose exec api python manage.py loaddata data/service.json