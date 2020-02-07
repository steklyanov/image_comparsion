FROM python:3.8-alpine
MAINTAINER Steklyanov Max

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN apk add --no-cache libc6-compat
RUN apk --no-cache add musl-dev linux-headers g++
RUN apk add --update --no-cache py3-numpy
ENV PYTHONPATH=/usr/lib/python3.8/site-packages
RUN echo 'manylinux1_compatible = True' > /usr/local/lib/python3.8/site-packages/_manylinux.py
RUN python -c 'import sys; sys.path.append(r"/_manylinux.py")'
RUN pip install --upgrade pip setuptools
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /image_comparsion
WORKDIR /image_comparsion
COPY ./image_comparsion /image_comparsion

RUN adduser -D user
USER user