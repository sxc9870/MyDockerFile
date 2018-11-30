from rediscluster import StrictRedisCluster

startup_nodes = [{"host": "172.172.0.4", "port": "6379"},{"host": "172.172.0.2", "port": "6379"},{"host": "172.172.0.3", "port": "6379"},{"host": "172.172.0.14", "port": "6379"},{"host": "172.172.0.12", "port": "6379"},{"host": "172.172.0.13", "port": "6379"}]

# Note: decode_responses must be set to True when used with python3
rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True, password='123456')

rc.set("foo", "bar")

print(rc.get("foo"))
