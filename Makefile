install:
	uv sync --dev

dev-start:
	uv run python manage.py runserver

migrate:
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --no-input


test:
	uv run pytest

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

test-coverage:
	uv run manage.py test --cov=task_manager --cov-report xml
