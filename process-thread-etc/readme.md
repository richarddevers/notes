# Thread, process, scheduler ,etc

source: <https://en.wikipedia.org/wiki/Thread_(computing>)

## The big picture

![alt text](process-thread.jpg "process-thread")

## thread

- the smallest sequence of programmed instructions that can be managed independently by a scheduler
- in most cases a thread is a component of a process
- thread of a process share ressources:
  - allocated memory
  - executable code
  - variables

## Process

## Thread vs Process

- Lower resource consumption of threads: using threads, an application can operate using fewer resources than it would need when using multiple processes.
- Simplified sharing and communication of threads: unlike processes, which require a message passing or shared memory mechanism to perform inter-process communication (IPC), threads can communicate through data, code and files they already share.
- Thread crashes a process: due to threads sharing the same address space, an illegal operation performed by a thread can crash the entire process; therefore, one misbehaving thread can disrupt the processing of all the other threads in the application.
