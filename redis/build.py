#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os


def buildeMode(argv):
    bindId = argv[2].replace(",", " \nbind ") #绑定IP 逗号分隔
    password = argv[3]#.input("请输入主节点密码：")  # 节点认证密码
    mOrs =argv[4] #input("请输入当前节点角色 m 还是s：")  # 是否主从
    masterIp =argv[5]  #input("从节点时指定主节点IP和端口(:分隔)：")  # 主节点iP端口 与哨兵同一个IP
    masterPort = masterIp.split(":")[1]  # 主节点端口
    masterIp = masterIp.split(":")[0]

    redisConf = ""
    sentinelConf = ""

    with open('src/redis.conf', 'r') as f:
        redisConf = f.read()
        if mOrs == "m":  # MASTER节点镜像
            redisConf = (redisConf % {'bIp': bindId, 'password': password, 'mk': "#", 'mIp': masterIp,
                                      'mPort': masterPort})
        else:
            redisConf = (redisConf % {'bIp': bindId, 'password': password, 'mk': "", 'mIp': masterIp,
                                      'mPort': masterPort})

    with open('src/sentinel.conf', 'r') as f:
        sentinelConf = f.read()
        if mOrs == "m":  # MASTER节点镜像
            sentinelConf = (sentinelConf % {'password': password, 'sName': "myMaster", 'sIp': masterIp,
                                            'sPort': masterPort})
        else:
            sentinelConf = (sentinelConf % {'password': password, 'sName': "myMaster", 'sIp': masterIp,
                                            'sPort': masterPort})

    with open('target/redis.conf', 'w') as f:
        f.write(redisConf)
    with open('target/sentinel.conf', 'w') as f:
        f.write(sentinelConf)

    with open('src/dockerfile', 'r') as f:
        with open('target/dockerfile', 'w') as f2:
            f2.write(f.read())
    cmd = ""  # build命令,启动命令
    if mOrs == "m":
        cmd = "cd target && docker build -t redis:master ."
    else:
        cmd = "cd target && docker build -t redis:slave%s-%s ." % (masterIp, masterPort)
    os.system(cmd)


def runModel(argv):
    containName = argv[2]  # 容器名称
    portExplose = argv[3].replace(",", " -p ")  # 暴露端口 多个用,分割
    imageName = argv[4]  # 镜像名称
    cmd = "cd target && docker run -itd --name %(name)s -p %(explose)s  %(imageName)s " % {"name": containName,
                                                                                           "explose": portExplose,
                                                                                           "imageName": imageName}
    os.system(cmd)


if __name__ == "__main__":
    type = sys.argv[1]
    if type == "b":  # 构建模式 用于build镜像
        buildeMode(sys.argv)
    elif type == "r":
        runModel(sys.argv)
