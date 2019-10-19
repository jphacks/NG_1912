FROM python:3.6.9-alpine3.10

LABEL maintainer="a.kamiya.208@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN apk update \
  # psycopg2 dependencies
  && apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev \
  && apk add --no-cache mariadb-dev \
  # Vue development dependencies
  && apk add --no-cache nodejs npm \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

WORKDIR /app

ENTRYPOINT ["/docker-entrypoint.sh"]
