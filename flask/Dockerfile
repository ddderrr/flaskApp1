# Build stage
FROM python:3.12-alpine3.22 AS build

WORKDIR /flask_app

RUN apk update && apk --no-cache add git gcc libc-dev libffi-dev curl

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --system --no-cache -r requirements.txt


# Application image
FROM python:3.12-alpine3.22

WORKDIR /flask_app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# copy python deps
COPY --from=build /usr/local/lib/python3.12/site-packages \
    /usr/local/lib/python3.12/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

COPY . /flask_app/

RUN chmod +x /flask_app/gunicorn_starter.sh


CMD ["./gunicorn_starter.sh"]

