run-server:
	uv run manage.py runserver

build:
	./build.sh

render-start:
	uv run gunicorn task_manager.wsgi