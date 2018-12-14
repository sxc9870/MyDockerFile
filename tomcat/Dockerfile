FROM tomcat:8.5.35-jre8-alpine

MAINTAINER  sxc 35631371@qq.com

#COPY redis.conf /usr/local/tomcat

RUN cd /etc/apk \
&& sed 's/http:\/\/dl-cdn.alpinelinux.org/https:\/\/mirrors.aliyun.com/g' -i /etc/apk/repositories \
&& apk update \
&& apk  --no-cache add curl
copy check_tomcat.sh /opt/check_tomcat.sh
HEALTHCHECK --interval=5s --timeout=2s --retries=12 CMD  sh /opt/check_tomcat.sh
#CMD ["catalina.sh", "run"]