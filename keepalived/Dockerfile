FROM alpine

MAINTAINER  sxc 35631371@qq.com

#/etc/conf.d/keepalived
#/etc/init.d/keepalived
#/etc/keepalived
#/usr/sbin/keepalived
copy keepalived-master.conf /etc/keepalived/keepalived-master.conf
copy keepalived-master.conf /etc/keepalived/keepalived-slave.conf

RUN cd /etc/apk \
&& sed 's/http:\/\/dl-cdn.alpinelinux.org/https:\/\/mirrors.aliyun.com/g' -i /etc/apk/repositories \
&& apk update \
&& apk  --no-cache add add keepalived curl iproute2