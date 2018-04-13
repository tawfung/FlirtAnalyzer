FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /EDfT
WORKDIR /EDfT
# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev
RUN pip install -U pip setuptools
COPY requirements.txt /EDfT/
COPY requirements-opt.txt /EDfT/
RUN pip install -r /EDfT/requirements.txt
RUN pip install -r /EDfT/requirements-opt.txt
ADD . /EDfT/
# Django service
EXPOSE 8000
