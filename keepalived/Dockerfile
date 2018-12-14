FROM alpine

MAINTAINER  sxc 35631371@qq.com

add keepalived-2.0.10.tar.gz  keepalived-2.0.10
RUN cd /etc/apk \
&& sed 's/http:\/\/dl-cdn.alpinelinux.org/https:\/\/mirrors.aliyun.com/g' -i /etc/apk/repositories \
&& apk update \
&& apk  --no-cache add keepalived