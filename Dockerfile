FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
ENV TZ=Europe/Warsaw
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY requirements.txt ./
RUN pip install -r requirements.txt