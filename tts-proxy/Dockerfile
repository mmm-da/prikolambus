FROM python:3.9.2-slim-buster

WORKDIR /tts-proxy
COPY ./requirements.txt /tts-proxy
RUN pip install -r requirements.txt
COPY ./ /tts-proxy/
