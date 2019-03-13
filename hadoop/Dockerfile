FROM jdk:base
MAINTAINER  sxc 35631371@qq.com

ENV HADOOP_HOME=/home/hadoop-3.1.2
ENV JAVA_HOME=/home/jdk/jdk1.8.0_201

copy hadoop-3.1.2 $HADOOP_HOME
copy core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml
copy hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml
copy mapred-site.xml $HADOOP_HOME/etc/hadoop/mapred-site.xml
copy yarn-site.xml $HADOOP_HOME/etc/hadoop/yarn-site.xml


RUN echo >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh  $JAVA_HOME