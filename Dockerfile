FROM python:3.7.4-alpine

RUN mkdir /usr/src/unammedAPI
WORKDIR /usr/src/unammedAPI

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install psycopg2
RUN apk add --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    openssl-dev \
    libffi-dev \
    libsodium-dev \
    build-base\
    && pip install psycopg2 && pip install pynacl && pip install cryptography --no-binary cr

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/unammedAPI/Pipfile
RUN pipenv install --skip-lock --system --dev

COPY . /usr/src/unammedAPI/