up:
	docker compose up

migrations:
	docker compose exec backend python manage.py makemigrations
	docker compose exec backend python manage.py migrate