#!/usr/bin/env bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
uv sync

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
# команду установки зависимостей, сборки статики, применения миграций и другие
make install && make collectstatic && make migrate