# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

WORKDIR /app

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY . requirements.txt /app/
RUN pip install -r requirements.txt


COPY . /app