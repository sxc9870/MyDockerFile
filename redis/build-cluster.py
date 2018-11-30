#from rediscluster import StrictRedisCluster

startup_nodes = [{"host": "172.172.0.4", "port": "6379"},
                 {"host": "172.172.0.2", "port": "6379"},
                 {"host": "172.172.0.3", "port": "6379"},
                 {"host": "172.172.0.14", "port": "6379"},
                 {"host": "172.172.0.12", "port": "6379"},
                 {"host": "172.172.0.13", "port": "6379"}]



#cluster-enabled yes（启动集群模式）
#cluster-config-file nodes-7000.conf（7000和port要对应）

dir="/usr/bin/redis.conf"
shutdownCmd="/usr/bin/redis-cli -a 123456 shutdown"
restartCmd="sh /usr/bin/redis.sh"

for a in startup_nodes:     # 第一个实例
    print(a["host"])




# Note: decode_responses must be set to True when used with python3
#rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True, password='123456')

#rc.set("foo", "bar")

#print(rc.get("foo"))
