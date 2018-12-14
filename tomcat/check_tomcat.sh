#!/bin/sh
wget --timeout=5 --tries=1 http://localhost:8080/ -q -O /dev/null
if [ $? == 1 ];then
    exit 1
else
     exit 0
fi
