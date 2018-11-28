#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os

def buildeMode(argv):
    bindId = argv[2]  # bindIp
    password = argv[3]  # 节点认证密码
    mOrs = argv[4]  # 是否主从
    masterIp = argv[5]  # 主节点iP
    masterPort = argv[6]  # 主节点端口
    redisConf = ""
    sentinelConf = ""

    with open('src/redis.conf', 'r') as f:
        redisConf = f.read()
        if mOrs == "m":  # MASTER节点镜像
            redisConf = (redisConf % {'bIp': bindId, 'password': password, 'mk': "#", 'mIp': masterIp,
                                      'mPort': masterPort})
        else:
            redisConf = (redisConf % (bindId, password, "", password, "", masterIp, masterPort))

    with open('src/sentinel.conf', 'r') as f:
        sentinelConf = f.read()
        if mOrs == "m":  # MASTER节点镜像
            sentinelConf = (sentinelConf % {'password': password, 'sName': "myMaster", 'sIp': masterIp,
                                            'sPort': masterPort})
        else:
            sentinelConf = (sentinelConf % (bindId, password, "", password, "", masterIp, masterPort))

    with open('target/redis.conf', 'w') as f:
        f.write(redisConf)
    with open('target/sentinel.conf', 'w') as f:
        f.write(sentinelConf)

    with open('src/dockerfile', 'r') as f:
        with open('target/dockerfile', 'w') as f2:
            f2.write(f.read())
    cmd=""  #build命令,启动命令
    if mOrs =="m":
      cmd="docker build -t sxc:master ."
    else :
      cmd="docker build -t sxc:slave%s%s  ." % (masterIp,":",masterPort)
    os.system("cd target")
    os.system(cmd)



def runModel(argv):
    containName=argv[2] #容器名称
    portExplose=argv[3] #暴露端口 多个用空格分割
    imageName=argv[4] #镜像名称
    cmd="docker run -itd --name %(name)s -p %(explose)s  %(imageName)s " % {"name":containName,"explose":portExplose,"imageName":imageName}
    os.system("cd target/")
    os.system(cmd)

if __name__ == "__main__":
    if (len(sys.argv)) < 1:
        print("参数不足:b模式,bindId,password,主从,主机IP和端口")
        sys.exit()
    type = sys.argv[1]
    if type == "b":  # 构建模式 用于build镜像
        buildeMode(sys.argv)
    else :
        runModel(sys.argv)