A=`ping -c 1 nginx 2>&1 `
echo $?

#if [ $A -eq 0 ];then
 #   nginx
  # sleep 2
   # if [ `ps -ef | grep nginx | grep -v grep | wc -l` -eq 0 ];then
        #killall keepalived
   #     ps -ef|grep keepalived|grep -v grep|awk '{print $2}'|xargs kill -9
   # fi

#fi/
