FROM python:3.7.4-slim-stretch

ENV PYTHONUNBUFFERED 1

RUN mkdir /dataframe_serialization_formats_analysis
WORKDIR /dataframe_serialization_formats_analysis

RUN apt-get -y update && apt-get -y install gcc

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
