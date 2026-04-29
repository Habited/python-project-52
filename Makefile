run-server:
	uv run manage.py runserver

build:
	./build.sh

render-start:
	uv run gunicorn task_manager.wsgi

run-shell:
	uv run manage.py shell

run-migration:
	uv run manage.py migrate

test:
	uv run coverage run manage.py test

test-coverage:
	coverage run manage.py test && coverage report -m
	coverage xml
