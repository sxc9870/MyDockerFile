#!/bin/sh
wget http://localhost:8080/
if [ $? == 1 ];then
    exit 1
else
     exit 0
fi
