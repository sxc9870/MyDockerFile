#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os


def buildeMode(argv):
    bindId = argv[1].replace(",", " \nbind ") #绑定IP 逗号分隔
    password = argv[2]#.input("请输入主节点密码：")  # 节点认证密码
    mOrs =argv[3] #input("请输入当前节点角色 m 还是s：")  # 是否主从
    masterIp =argv[4]  #input("从节点时指定主节点IP和端口(:分隔)：")  # 主节点iP端口 与哨兵同一个IP
    masterPort = masterIp.split(":")[1]  # 主节点端口
    masterIp = masterIp.split(":")[0]
    mk = ""
    if argv[5] != "c":
       mk="#"    #集群模式不允许slaveofxxx
       cluster=""
    else:
       cluster = "#"

    mk_server=""
    mk_sentinel="##"
    redisConf = ""

    if mOrs == "m":  # MASTER节点镜像
        mk="#"
    with open('src/redis.conf', 'r') as f:
            redisConf = f.read()

            redisConf = (redisConf % {'bIp': bindId, 'password': password, 'mk': mk, 'mIp': masterIp,
                                          'mPort': masterPort,"cluster":cluster})

    with open('target/redis.conf', 'w') as f:
            f.write(redisConf)


    with open('src/dockerfile', 'r') as f:
        with open('target/dockerfile', 'w') as f2:
            f2.write(f.read() % {"mk_server":mk_server,"mk_sentinel":mk_sentinel})
    cmd = ""  # build命令,启动命令
    if mOrs == "m":
        cmd = "cd target && docker build -t redis:master-server  ."
    else:
        cmd = "cd target && docker build -t redis:slave-server ."
    os.system(cmd)



if __name__ == "__main__":
    buildeMode(sys.argv)
