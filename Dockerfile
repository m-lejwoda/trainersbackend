FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
ENV TZ=Europe/Warsaw
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY requirements.txt ./
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow
# RUN apt-get update
# RUN apt-get install python-dev
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
# RUN apt-get install python3-all-dev
# RUN apt-get install --no-cache \
#         uwsgi-python3 \
#         python3
# RUN apt-get install --update --no-cache --virtual .tmp linux-headers
RUN pip install -r requirements.txt

COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
# USER user 

CMD ["entrypoint.sh"]