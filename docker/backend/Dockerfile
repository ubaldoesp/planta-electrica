FROM python:3.7.12-alpine3.15

ENV PYTHONUNBUFFERED 1

ARG APP=/app
ARG APP_USER

RUN apk add --no-cache --virtual .build-deps build-base \
    linux-headers postgresql-dev
RUN apk add --no-cache libffi-dev jpeg-dev zlib-dev \
    zeromq-dev \
    openssl-dev \
    postgresql-client \
    postgresql-libs

WORKDIR ${APP}

COPY . ${APP}

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN apk --purge del .build-deps

ENTRYPOINT [ "/app/docker/backend/docker-entrypoint.sh" ]

CMD ["runserver"]
