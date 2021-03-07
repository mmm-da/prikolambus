FROM python:3.9.2-slim-buster

WORKDIR /anekdoter
COPY ./requirements.txt /anekdoter
RUN pip install -r requirements.txt
COPY ./ /anekdoter/
