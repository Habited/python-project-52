install:
	uv sync

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
	uv run coverage run pytest
	uv run coverage report --show-missing --skip-covered

ci-install:
	uv sync --group dev

ci-migrate:
	uv run python manage.py makemigrations --noinput && \
	uv run python manage.py migrate --noinput

ci-test:
	uv run coverage run pytest
	uv run coverage xml
	uv run coverage report --show-missing --skip-covered
