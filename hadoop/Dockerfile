FROM jdk:base
MAINTAINER  sxc 35631371@qq.com

ENV HADOOP_HOME=/home/hadoop-3.1.2
ENV JAVA_HOME=/home/jdk/jdk1.8.0_201


add hadoop-3.1.2.tar.gz $HADOOP_HOME
copy etc $HADOOP_HOME


#RUN echo >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh  export JAVA_HOME=$JAVA_HOME