# Thread, process, scheduler and family

## Source

- <https://en.wikipedia.org/wiki/Process_(computing>)
- <https://en.wikipedia.org/wiki/Thread_(computing>>)
- <https://en.wikipedia.org/wiki/Subroutine>
- <https://en.wikipedia.org/wiki/Thread_(computing>)
- <https://en.wikipedia.org/wiki/Cooperative_multitasking>
- <https://en.wikipedia.org/wiki/Preemption_(computing)#PREEMPTIVE>
- <https://en.wikipedia.org/wiki/Generator_(computer_programming)>)

## The big picture

![alt text](process-thread.jpg "process-thread")

## Preemption

Act of temporarily interrupting an executing task, with the intention of resuming it at a later time

## Preemptive multitasking

The os kernel, using the scheduler (and his policy) may interrupt suspends the execution of a process to run another one.

## Non-preemptive multitasking (a.k.a Cooperative multitasking)

The context switch is not initiated by the operating system but by the process.

The process voluntarily yield controld perdicallly or when idle or logically blocked.

The os scheduler then select the next task to be execute.

## Process

Instance of a program executed by one or many threads.

- contains program code and activity
- execution of a program (ram instanciation)

## Thread

- the smallest sequence of programmed instructions that can be managed independently by a scheduler
- in most cases a thread is a component of a process
- thread of a process share ressources:
  - allocated memory
  - executable code
  - variables

## Thread vs Process

- Lower resource consumption of threads: using threads, an application can operate using fewer resources than it would need when using multiple processes.
- Simplified sharing and communication of threads: unlike processes, which require a message passing or shared memory mechanism to perform inter-process communication (IPC), threads can communicate through data, code and files they already share.
- Thread crashes a process: due to threads sharing the same address space, an illegal operation performed by a thread can crash the entire process; therefore, one misbehaving thread can disrupt the processing of all the other threads in the application.

## Subroutine (a.k.a routine)

Subroutine = sequence execution. Sync. When invoke, never yield, just finished, no state management.

An instance of a subroutine only returns once, and does not hold state between invocations

Depending on the context, can be called:

- routine
- subprogram
- function
- method
- procedure
- callable unit

## Coroutines

subroutine for non-preemptive multitasking.

Allow suspension and resum of the execution (yield)

State management

## Generators

Routine that control the iteration of a loop
