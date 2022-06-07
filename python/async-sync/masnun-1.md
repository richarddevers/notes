# Async Python: The Different Forms of Concurrency

source:

- <http://masnun.rocks/2016/10/06/async-python-the-different-forms-of-concurrency/>

- <https://medium.com/contentsquare-engineering-blog/multithreading-vs-multiprocessing-in-python-ece023ad55a>

## Sync

task executed one after another. You have to wait the end of the previous task before starting the next one. Blocking

## Async

task can be paused. when a task paused, another one can start. Non blocking

## Concurrency

Managing the context switching between differents tasks. But only one task is executed at a time. However, this can give the illusion of parallelism.

## Parallelism

Multiple tasks are run **at the same time**

## Recap

- Sync: Blocking operations.
- Async: Non blocking operations.
- Concurrency: Making progress together.
- Parallelism: Making progress in parallel.

**Parallelism implies Concurrency. But Concurrency doesn’t always mean Parallelism**

## Threads

Python threads allow concurrency.

But GIL allow only one threads at a time, so no parallelism.

## Global Interpreter Lock (GIL)

What?

- ensure the python interpreter run one thred at a time

Why?

- easier memory management
- better integrations with C
- GIL makes it easy to integrate non thread safe C libraries (???)

How?

- the python interpreter switch between threads to allow concurrency

Facts

- The most common python implementation is CPython (which has GIL). However, not every implementations have GIL. Jython for eg doesn't have GIL.
- single threaded programs are fast thanks to the GIL
- for I/O bound operations, GIL usually doesn't harm much (i guess depending on the quantity?)
- for CPU bound task, the interpreter siwtch between n ticks and switch.

see: <http://www.dabeaz.com/python/UnderstandingGIL.pdf> (that links hurts a little bit)

## MultiProcessing

To get parallelism -> multiprocessing

allow python to spawn multiple process that can run in //

see: <https://pymotw.com/3/multiprocessing/index.html>

## Multithreading

Concurrent. You stil have the GIL, so only one thread at a time.

Good for I/O bound operation.

If one thread wait for an I/O, another one can work.

Basically ancestry of async/await (asyncio) syntax .

Hard to manage. You can easyly mess up. But it exist.

## Asyncio

Why?
- Process are costly to spawn/manage
- multithreading is hard to code/debug/evolv/manage and so on...
- threads started at the same time must still wait that all are ready before going on to something else

How?

- Event loop: tracks differents I/O events and switch to tasks which are ready and pauses the ones waiting for I/O
- The event loop is composes of functions and the event loop return a Future object (https://docs.python.org/3/library/asyncio-future.html)

Asyncio  uses generators and coroutines to pause and resume tasks.
see:
- https://masnun.com/2015/11/20/python-asyncio-future-task-and-the-event-loop.html
- https://masnun.com/2015/11/13/python-generators-coroutines-native-coroutines-and-async-await.html


# Which ones?

- CPU Bound => Multi Processing
- I/O Bound, Fast I/O, Limited Number of Connections => Multi Threading
- I/O Bound, Slow I/O, Many connections => Asyncio
