release: python smvsite/manage.py collectstatic
release: python smvsite/manage.py migrate
web: gunicorn --pythonpath smvsite smvsite.wsgi