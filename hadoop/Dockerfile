FROM java:8-jre

MAINTAINER  sxc 35631371@qq.com
copy hadoop-3.1.2 /home/hadoop-3.1.2
RUN cd /etc/apk \
&& sed 's/http:\/\/dl-cdn.alpinelinux.org/https:\/\/mirrors.aliyun.com/g' -i /etc/apk/repositories \
&& apk update \
&& apk  --no-cache add    curl