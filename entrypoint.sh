#!/bin/sh
echo "Starting migrations for project..."
python /code/manage.py makemigrations
python /code/manage.py migrate --noinput
echo "Starting migrations for app..."
python /code/manage.py makemigrations account
python /code/manage.py migrate account --noinput
python /code/manage.py makemigrations article
python /code/manage.py migrate article --noinput
echo "Migrations ended!"
python /code/manage.py createcustomsuperuser
python /code/manage.py collectstatic --noinput
exec "$@"