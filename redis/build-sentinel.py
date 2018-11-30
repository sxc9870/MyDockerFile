#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os


def buildeMode(argv):
    bindId = argv[1].replace(",", " \nbind ")  # 绑定IP 逗号分隔
    password = argv[2]#.input("请输入主节点密码：")  # 节点认证密码
    masterIp =argv[3]  #input("从节点时指定主节点IP和端口(:分隔)：")  # 主节点iP端口 与哨兵同一个IP
    masterPort = masterIp.split(":")[1]  # 主节点端口
    masterIp = masterIp.split(":")[0]
    mk_server="##"
    mk_sentinel=""
    sentinelConf = ""
    with open('src/sentinel.conf', 'r') as f:
            sentinelConf = f.read()
            sentinelConf = (sentinelConf % {"bindId":bindId,'password': password, 'sName': "myMaster", 'sIp': masterIp,
                                                'sPort': masterPort})

    with open('target/sentinel.conf', 'w') as f:
            f.write(sentinelConf)
    with open('src/dockerfile', 'r') as f:
        with open('target/dockerfile', 'w') as f2:
            f2.write(f.read() % {"mk_server":mk_server,"mk_sentinel":mk_sentinel})
    cmd = ""  # build命令,启动命令

    cmd = "cd target && docker build -t redis:sentinel  ."

    os.system(cmd)



if __name__ == "__main__":

    buildeMode(sys.argv)
