FROM python:3.9

ENV PYTHONUNBUFFERED 1
COPY requirements.txt /requirements.txt
COPY . /newsboard

WORKDIR /newsboard
EXPOSE 8000

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

USER root
