#docker rmi $(docker images -aq) -f && docker rm $(docker ps -aq) -f
docker-compose -f docker-compose.yml -f docker-sentinel.yml up -d
