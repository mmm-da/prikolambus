FROM python:3.9.2-slim-buster

WORKDIR /generator
COPY ./requirements.txt /generator
RUN pip install -r requirements.txt
COPY ./ /generator
