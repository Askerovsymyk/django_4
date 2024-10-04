FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNDUFFERED 1

WORKDIR /app

COPY reguarement.txt /app/reguarement.txt

RUN pip install -r /app/reguarement.txt

COPY . .