FROM   centos:7
MAINTAINER  sxc 35631371@qq.com

add jdk_1.8.tar.gz /home/jdk

run echo >> /etc/profile 'export JAVA_HOME=/home/jdk/jdk1.8.0_202'\
&& echo >> /etc/profile 'export PATH=$JAVA_HOME/bin:$PATH'\
&& echo >> /etc/profile 'export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar'