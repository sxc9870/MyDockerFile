for server in $HADOOP_SERVERS; do
        echo "$server" >> "/etc/hosts"
done