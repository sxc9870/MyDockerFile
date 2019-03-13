FROM jdk:base
MAINTAINER  sxc 35631371@qq.com

add hadoop-3.1.2.tar.gz /home/hadoop

ENV HADOOP_HOME=/home/hadoop/hadoop-3.1.2
ENV JAVA_HOME=/home/jdk/jdk1.8.0_201



copy etc $HADOOP_HOME/etc


#RUN echo >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh  export JAVA_HOME=$JAVA_HOME