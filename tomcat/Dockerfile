FROM tomcat:8.5.35-jre8-alpine

MAINTAINER  sxc 35631371@qq.com
ARG cluster



COPY redis.conf /redis.conf
COPY sentinel.conf /sentinel.conf

RUN echo  >>  /redis.conf ${cluster}cluster-enabled yes \
&&  echo  >>  /redis.conf ${cluster}cluster-config-file nodes-6379.conf \
&&  echo  >> /redis.conf  ${cluster}cluster-node-timeout 15000

#CMD [ "redis-server", "/redis.conf"  ]