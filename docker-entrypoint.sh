#!/bin/sh
python manage.py makemigrations  --no-input
python manage.py migrate  --no-input
python manage.py collecstatic --no-input
gunicorn bookproject.wsgi:application --timeout 120 --workers=3 --threads=3 --worker-connections=1000 --bind 0.0.0.0:8000