# CMD

## Run overridding CMD

docker run {image} {args}

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

## Image layer

docker history {{image-name }}


# Dockerfile keyword

WORKDIR: create a directory and cd inside

ENTRYPOINT: create an executable and put it in the path. Launch a process and can have arguments. PID1

CMD: Same. Provide argument for ENTRYPOINT if provided. CMD is the default but 

ENTRYPOINT is always run. CMD can be override by user (*docker run {image} {cmd}*)

USER: By default, user is root. USER can set a new user (USER 1001 for eg) with RO access to everything except RW to /tmp.

 
# PID1 , exec ...

ENTRYPOINT is PID 1 (first process). 

Stop signal is send to PID1. 

But if ENTRYPOINT run another shell (*sh -c hello*...) , the second process will not receive the termination signal.

You can still kill it withc *docker stop*

To avoid that:
 - use exec so the second process will have PID1 (sh -c exec hello)
 - use only one process (no *sh -c*, just *hello*)
 - tini (*tini -g -- sh -c hello*), must be enable at run (*docker run --init -e TINI_KILL_PROCESS_GROUP=1*)