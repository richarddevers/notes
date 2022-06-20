source: <https://ncrocfer.github.io/posts/celery-importance-pool-execution/>

## Execution Pool

== Execution mode of specific task.

It's a worker settings.

### Usage

### prefork

default. Parrallelle mode.

Multiprocessing. Celery will spawn as many process as your cpu core.

Good for CPU Bound

```console

celery -A tasks worker

ps -A | grep -i celery
```

### solo

Worker thread will execute task.

```console

celery -A tasks worker -P solo

```

### gevent

Concurrent mode.

Good for IO bound.

```console

celery -A tasks worker -P solo

```
