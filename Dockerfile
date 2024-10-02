FROM python:3.11-alpine3.18
LABEL maintainer='tiomashimon'

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -rf /tmp

COPY . .

EXPOSE 8000

CMD ["scripts/run.sh"]
