FROM jdk:base
MAINTAINER  sxc 35631371@qq.com

add hadoop-3.1.2.tar.gz /home/hadoop

ENV HADOOP_HOME=/home/hadoop/hadoop-3.1.2
#ENV JAVA_HOME=/home/jdk/jdk1.8.0_201



copy config/etc $HADOOP_HOME/etc
copy config/sbin $HADOOP_HOME/sbin

RUN mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo_bak\
&& yum -y install wget\
&& wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo\
&& yum makecache  && yum -y update\
&& yum install openssh-server -y\
&& yum install net-tools -y