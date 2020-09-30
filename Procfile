release: python smvsite/manage.py collectstatic --noinput
release: python smvsite/manage.py migrate
web: gunicorn --pythonpath smvsite smvsite.wsgi