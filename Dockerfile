FROM python:alpine

ENV PYTHONUNBUFFERED 1

RUN apk update --no-cache && apk upgrade --no-cache

RUN apk add --no-cache postgresql-libs zlib-dev jpeg-dev

RUN apk add --no-cache --virtual .build-deps postgresql-dev gcc musl-dev

WORKDIR /code

COPY requirements.txt /code

RUN pip install --no-cache-dir -r requirements.txt

RUN apk --purge del .build-deps

COPY . /code

RUN mkdir /code/smvsite/media

WORKDIR /code/smvsite

RUN python manage.py collectstatic --noinput

CMD gunicorn -b 0.0.0.0:8000 smvsite.wsgi
