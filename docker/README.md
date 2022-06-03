# CMD

## Delete unused images

docker image prune -a

## Delete container exited and not run for weeks

docker ps --filter "status=exited" | grep 'weeks ago'  | awk '{print $1}'  | xargs docker rm

## Delete container exited and not run for months

docker ps --filter "status=exited" | grep 'months ago'  | awk '{print $1}'  | xargs docker rm

## Delete all stopped containers

docker rm $(docker ps -a -q)

## Nuke

docker kill -f \$(docker ps -a -q) && docker rm -f \$(docker ps -a -q) && docker rmi -f $(docker images -a -q)
