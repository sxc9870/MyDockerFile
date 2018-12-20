#!/bin/sh
#wget --timeout=5 --tries=1 http://localhost:8081/service/metrics/ping -q -O /dev/null
curl -u admin:admin123 http://localhost:8081/service/metrics/ping
if [ $? == 1 ];then
    exit 1    #考虑KILL1 让容器停止以后自动重启
else
     exit 0
fi
