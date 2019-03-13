FROM   centos:7
MAINTAINER  sxc 35631371@qq.com

add jdk_1.8.tar.gz /home/jdk
ENV JAVA_HOME=/home/jdk/jdk1.8.0_201
ENV PATH=$JAVA_HOME/bin:$PATH
ENV CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar

run yum -y update && yum -y install passwd openssl openssh-server  openssh-clients &&mkdir  /var/run/sshd/