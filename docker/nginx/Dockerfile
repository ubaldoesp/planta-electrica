FROM nginx:stable-alpine

ARG CONFIG_ROOT=./docker/nginx/dev

RUN rm /etc/nginx/conf.d/default.conf

COPY ${CONFIG_ROOT}/nginx.conf /etc/nginx/
COPY ${CONFIG_ROOT}/sites-enabled /etc/nginx/sites-enabled
