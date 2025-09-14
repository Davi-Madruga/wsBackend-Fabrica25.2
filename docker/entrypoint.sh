#!/bin/sh
set -e
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

#certifique de estar com a LF(Line Feed) 
#para executar levantar o container