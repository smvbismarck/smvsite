cd smvsite
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn smvsite.wsgi