# Python asyncio: Future, Task and the Event Loop

source: https://masnun.com/2015/11/20/python-asyncio-future-task-and-the-event-loop.html

## Event loop

The event loop register tasks to be executed then monitor them so it can execute, delay or cancel them..

the loop run one function, while the function waits for I/O it pauses it and runs another one.

## Futur/Task

Futur: an object that is supposed to have a result in the future (a promise)

Task: subclass of Future; Wraps it into a coroutine. When the coroutine is finished, the result taks is realized.


## Coroutines

Function that can "pause" and return a series of values periodiccallt.

Based on **yield** or **await** syntax

## Usage

coroutine=> task