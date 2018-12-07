FROM redis:5.0.2-alpine

MAINTAINER  sxc 35631371@qq.com
ARG password
#RUN echo "$password"

COPY redis.conf /redis.conf
COPY sentinel.conf /sentinel.conf
#CMD [ "redis-server", "/redis.conf"  ]