FROM sonatype/nexus3:latest

MAINTAINER  sxc 35631371@qq.com
copy check_nexus.sh /opt/check_nexus.sh
HEALTHCHECK --interval=5s --timeout=2s --retries=12 CMD   sh /opt/check_nexus.sh
#CMD ["catalina.sh", "run"]