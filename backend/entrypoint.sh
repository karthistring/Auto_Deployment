#!/bin/sh

python manage.py makemigrations --no-input
python manage.py migrate --no-input


gunicorn docker_demo.wsgi:application --bind 0.0.0.0:7777
