docker exec -it mq2 /bin/bash
rabbitmqctl stop_app
rabbitmqctl reset
rabbitmqctl join_cluster rabbit@mq1
rabbitmqctl start_app
exit


docker exec -it mq3 /bin/bash
rabbitmqctl stop_app
rabbitmqctl reset
rabbitmqctl join_cluster rabbit@mq1
rabbitmqctl start_app
exit

