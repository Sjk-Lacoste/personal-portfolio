release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn core.wsgi --log-file -
