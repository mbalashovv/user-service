FROM python:3.12-bookworm

WORKDIR /usr/src/migrations/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends dos2unix

RUN pip install --upgrade pip && pip install poetry

COPY poetry.lock pyproject.toml poetry.toml /usr/src/migrations/

RUN poetry install --no-dev

COPY . /usr/src/migrations/

#RUN dos2unix scripts/*
