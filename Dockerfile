FROM python:3.8-buster

WORKDIR /opt/app
COPY . /opt/app

RUN pip3 install -r requirements.txt
