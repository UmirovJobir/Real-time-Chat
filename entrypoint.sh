#!/bin/bash


echo "Apply database migrations"
python3 manage.py makemigrations
python3 manage.py migrate

daphne a_core.asgi:application -b 0.0.0.0:5000 


exec "$@"