#!/bin/sh
FROM alpine:3.8

# RUN apk update && apk add bash nano curl \
RUN apk update && apk add \
        python3 \
        # python3-dev \
        uwsgi-python3

RUN addgroup -S django && adduser -S -G django django
RUN mkdir -p /usr/src/app/mysite
WORKDIR /usr/src/app

ADD site/setup.py \
    site/requirements.txt \
    /usr/src/app/
RUN pip3 install --upgrade pip && pip3 install -U -e .
COPY site /usr/src/app/

ENV DJANGO_SETTINGS_MODULE mysite.settings.local

COPY configs/uwsgi-entrypoint.ini /configs/
VOLUME /usr/src/app
EXPOSE 8001
CMD [ "uwsgi", "--ini", "/configs/uwsgi-entrypoint.ini" ]