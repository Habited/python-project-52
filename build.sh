#!/usr/bin/env bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
uv sync --frozen

# Convert static asset files
python manage.py collectstatic --noinput

# Apply any outstanding database migrations
python manage.py migrate
