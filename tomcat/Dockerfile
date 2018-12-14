FROM tomcat:8.5.35-jre8-alpine

MAINTAINER  sxc 35631371@qq.com

#COPY redis.conf /usr/local/tomcat
HEALTHCHECK --interval=5s --timeout=2s --retries=12 CMD curl --fail http://localhost:8080/ || echo 111
#CMD ["catalina.sh", "run"]