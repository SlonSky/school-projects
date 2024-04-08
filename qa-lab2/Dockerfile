FROM python:3.6
ENV PYTHONBUFFERED 1

RUN mkdir -p /config
RUN mkdir -p /lab

COPY ./config /config
COPY . /lab
RUN ls /lab && ls lab/tests
ENV PYTHONPATH /lab/
WORKDIR /lab

RUN apt-get update && apt-get -y install mysql-server
RUN pip install -r /config/requirements.txt
