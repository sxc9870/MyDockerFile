#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os




def runModel(argv):
    containName = argv[1]  # 容器名称
    portExplose = argv[2].replace(",", " -p ")  # 暴露端口 多个用,分割
    imageName = argv[3]  # 镜像名称
    networkName = argv[4]  # docker net节点名称
    ip = argv[5]  # 指定容器IP
    cmd = "cd target && docker run -itd  --name %(name)s --network %(networkName)s --ip %(ip)s  -p %(explose)s  %(imageName)s " % {"name": containName,
                                                                                           "explose": portExplose,"ip":ip,"networkName":networkName,
                                                                                           "imageName": imageName}
    os.system(cmd)


if __name__ == "__main__":

        runModel(sys.argv)