FROM python:alpine

ENV PYTHONUNBUFFERED 1

RUN apk update --no-cache && apk upgrade --no-cache

RUN apk add --no-cache postgresql-libs

RUN apk add --no-cache --virtual .build-deps postgresql-dev gcc musl-dev

WORKDIR /code

COPY requirements.txt /code

RUN pip install --no-cache-dir -r requirements.txt

RUN apk --purge del .build-deps

COPY . /code

CMD python smvsite/manage.py migrate && gunicorn -b 0.0.0.0:8000 --pythonpath smvsite smvsite.wsgi