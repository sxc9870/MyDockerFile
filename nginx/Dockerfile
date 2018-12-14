FROM nginx:1.15.7-alpine

MAINTAINER  sxc 35631371@qq.com





copy check_nginx.sh /opt/check_nginx.sh
HEALTHCHECK --interval=5s --timeout=2s --retries=12 CMD   sh /opt/check_nginx.sh