#!/bin/sh
wget --timeout=5 --tries=1 http://localhost:8080/ -q -O /dev/null
if [ $? == 1 ];then
    exit 1    #考虑KILL1 让容器停止以后自动重启
else
     exit 0
fi
