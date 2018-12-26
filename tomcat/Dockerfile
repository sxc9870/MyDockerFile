FROM tomcat:8.5.35-jre8-alpine

MAINTAINER  sxc 35631371@qq.com



COPY tomcat-users.xml /usr/local/tomcat/conf/
copy check_tomcat.sh /opt/check_tomcat.sh
HEALTHCHECK --interval=5s --timeout=2s --retries=12 CMD   sh /opt/check_tomcat.sh
#CMD ["catalina.sh", "run"]