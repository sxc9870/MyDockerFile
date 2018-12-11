FROM nginx:1.15.7-alpine

MAINTAINER  sxc 35631371@qq.com
#COPY static-html-directory /usr/share/nginx/html
#COPY redis.conf /usr/local/tomcat
COPY nginx.conf.default /etc/nginx/nginx.conf
COPY vhost.conf /etc/nginx/vhost.conf
COPY web1.conf /etc/nginx/web1.conf
COPY static /data/nginx/static