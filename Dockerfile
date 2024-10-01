FROM python:3.12-bullseye

ENV PYTHONBUFFERED=1
#
#RUN mkdir code
WORKDIR /django
#
#ADD . /code/
#ADD .env.docker /code/.env
#
#ENV APP_NAME=MAIN

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY . .

CMD python manage.py runserver 0.0.0.0:8000

